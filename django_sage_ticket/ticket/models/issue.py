from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from django_sage_ticket.ticket.helper.mixins import TimeStampMixin
from django_sage_ticket.ticket.helper import SeverityEnum, TicketStateEnum


class Issue(TimeStampMixin):
    """Model to represent an issue in the django_sage_ticket ticketing
    system."""

    subject = models.CharField(
        max_length=255,
        verbose_name=_("Subject"),
        help_text=_("The subject of the issue."),
        db_comment="The subject of the issue.",
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the issue reporter."),
        db_comment="The name of the issue reporter.",
    )
    message = models.TextField(
        verbose_name=_("Message"),
        help_text=_("The detailed message of the issue."),
        db_comment="The detailed message of the issue.",
    )
    severity = models.CharField(
        max_length=20,
        choices=SeverityEnum.choices,
        verbose_name=_("Severity"),
        help_text=_("The severity level of the issue."),
        db_comment="The severity level of the issue.",
    )
    raised_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Raised by"),
        on_delete=models.CASCADE,
        help_text=_("The user who raised the issue."),
        db_comment="The user who raised the issue.",
    )
    department = models.ForeignKey(
        "Department",
        verbose_name=_("Department"),
        on_delete=models.CASCADE,
        help_text=_("The department to which the issue is assigned."),
        db_comment="The department to which the issue is assigned.",
    )
    state = models.CharField(
        choices=TicketStateEnum.choices,
        max_length=20,
        verbose_name=_("State"),
        help_text=_("The current state of the issue."),
        db_comment="The current state of the issue.",
    )
    is_unread = models.BooleanField(
        verbose_name=_("Is Unread"),
        default=False,
        help_text=_("Indicates if the issue is unread."),
        db_comment="Indicates if the issue is unread.",
    )
    is_archive = models.BooleanField(
        verbose_name=_("Is Archive"),
        default=False,
        help_text=_("Indicates if the issue is archived."),
        db_comment="Indicates if the issue is archived.",
    )

    class Meta:
        verbose_name = _("Issue")
        verbose_name_plural = _("Issues")
        db_table = "issue"
        constraints = [
            models.CheckConstraint(
                name="issue_state", check=models.Q(state__in=TicketStateEnum.values)
            )
        ]

    def clean(self):
        """Validate the issue's state transitions and ensure the state value is
        valid."""
        super().clean()

        if self.state not in TicketStateEnum.values:
            raise ValidationError(_("Invalid state value"))

        current_state = None
        if self.pk is not None:  # check if data is being updated
            current_state = Issue.objects.get(pk=self.pk).state

        valid_states = Issue.get_valid_states()
        if current_state is not None and self.state not in valid_states.get(
            current_state, []
        ):
            raise ValidationError(
                _(f"Invalid state transition from {current_state} to {self.state}")
            )

    @staticmethod
    def get_valid_states():
        """Get the valid state transitions for an issue."""
        valid_state = {
            "new": ["open", "closed"],
            "open": ["pending", "closed"],
            "pending": ["hold", "closed"],
            "hold": ["resolved", "closed"],
            "resolved": ["closed"],
            "closed": ["new"],
        }
        return valid_state

    def __repr__(self):
        return f"<Issue(id={self.id}, subject={self.subject}, state={self.state})>"

    def __str__(self):
        return self.subject
