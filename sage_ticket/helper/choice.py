from django.db import models


class SeverityEnum(models.TextChoices):
    """SeverityEnum is an enumeration that represents different levels of
    severity for issues or tasks.

    It is used to categorize the criticality or importance of a given
    item.

    """

    HIGH = ("high", "High")
    MEDIUM = ("medium", "Medium")
    LOW = ("low", "Low")


class TicketStateEnum(models.TextChoices):
    """TicketStateEnum is an enumeration that represents the different states
    that a ticket can have during its lifecycle in a ticketing or issue
    tracking system."""

    NEW = ("new", "New")
    OPEN = ("open", "Open")
    PENDING = ("pending", "Pending")
    HOLD = ("hold", "Hold")
    RESOLVED = ("resolved", "Resolved")
    CLOSED = ("closed", "Closed")


class ExtensionsEnum(models.TextChoices):
    """ExtensionsEnum is an enumeration that represents different file
    extensions that may be associated with attachments or other resources in
    the system."""

    pdf = ("pdf", "PDF")
    jpg = ("jpg", "JPEG")
    png = ("png", "PNG")
    webp = ("webp", "WebP")


class StatusEnum(models.TextChoices):
    """StatusEnum is an enumeration that represents the status of a response or
    inquiry in a communication or ticketing system."""

    ANSWERED = ("answered", "Answered")
    UNANSWERED = ("unanswered", "Unanswered")
