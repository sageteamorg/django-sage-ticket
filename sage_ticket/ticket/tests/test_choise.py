import os

import django
from django.conf import settings

from sage_ticket.ticket.helper.choice import (
    ExtenstionsEnum,
    SeverityEnum,
    StatusEnum,
    TicketStateEnum,
)

if not settings.configured:
    os.environ["DJANGO_SETTINGS_MODULE"] = "kernel.settings"
    django.setup()


class TestSeverityEnum:
    def test_severity_enum_values(self):
        assert SeverityEnum.HIGH.value == "high"
        assert SeverityEnum.MEDIUM.value == "medium"
        assert SeverityEnum.LOW.value == "low"

    def test_severity_enum_labels(self):
        assert SeverityEnum.HIGH.label == "High"
        assert SeverityEnum.MEDIUM.label == "Medium"
        assert SeverityEnum.LOW.label == "Low"


class TestTicketStateEnum:
    def test_ticket_state_enum_values(self):
        assert TicketStateEnum.NEW.value == "new"
        assert TicketStateEnum.OPEN.value == "open"
        assert TicketStateEnum.PENDING.value == "pending"
        assert TicketStateEnum.HOLD.value == "hold"
        assert TicketStateEnum.RESOLVED.value == "resolved"
        assert TicketStateEnum.CLOSED.value == "closed"

    def test_ticket_state_enum_labels(self):
        assert TicketStateEnum.NEW.label == "New"
        assert TicketStateEnum.OPEN.label == "Open"
        assert TicketStateEnum.PENDING.label == "Pending"
        assert TicketStateEnum.HOLD.label == "Hold"
        assert TicketStateEnum.RESOLVED.label == "Resolved"
        assert TicketStateEnum.CLOSED.label == "Closed"


class TestExtenstionsEnum:
    def test_extensions_enum_values(self):
        assert ExtenstionsEnum.pdf.value == "pdf"
        assert ExtenstionsEnum.jpg.value == "jpg"
        assert ExtenstionsEnum.png.value == "png"
        assert ExtenstionsEnum.webp.value == "webp"

    def test_extensions_enum_labels(self):
        assert ExtenstionsEnum.pdf.label == "PDF"
        assert ExtenstionsEnum.jpg.label == "JPEG"
        assert ExtenstionsEnum.png.label == "PNG"
        assert ExtenstionsEnum.webp.label == "WebP"


class TestStatusEnum:
    def test_status_enum_values(self):
        assert StatusEnum.ANSWERED.value == "answered"
        assert StatusEnum.UNANSWERED.value == "unanswered"

    def test_status_enum_labels(self):
        assert StatusEnum.ANSWERED.label == "Answered"
        assert StatusEnum.UNANSWERED.label == "Unanswered"


class TestEnumUsageInModel:
    def test_severity_enum_usage_in_model(self):
        # Assuming a model with a severity field using SeverityEnum
        from sage_ticket.ticket.models import Issue

        issue = Issue(severity=SeverityEnum.HIGH)
        assert issue.severity == SeverityEnum.HIGH

    def test_ticket_state_enum_usage_in_model(self):
        # Assuming a model with a state field using TicketStateEnum
        from sage_ticket.ticket.models import Issue

        issue = Issue(state=TicketStateEnum.NEW)
        assert issue.state == TicketStateEnum.NEW

    def test_extensions_enum_usage_in_model(self):
        # Assuming a model with an extensions field using ExtenstionsEnum
        from sage_ticket.ticket.models import Attachment

        attachment = Attachment(extensions=ExtenstionsEnum.pdf)
        assert attachment.extensions == ExtenstionsEnum.pdf

    def test_status_enum_usage_in_model(self):
        # Assuming a model with a status field using StatusEnum
        from sage_ticket.ticket.models import Comment

        comment = Comment(status=StatusEnum.ANSWERED)
        assert comment.status == StatusEnum.ANSWERED
