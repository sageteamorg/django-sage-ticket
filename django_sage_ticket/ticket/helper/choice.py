from django.db import models


class SeverityEnum(models.TextChoices):
    HIGH = ("high", "High")
    MEDIUM = ("medium", "Medium")
    LOW = ("low", "Low")


class TicketStateEnum(models.TextChoices):
    NEW = ("new", "New")
    OPEN = ("open", "Open")
    PENDING = ("pending", "Pending")
    HOLD = ("hold", "Hold")
    RESOLVED = ("resolved", "Resolved")
    CLOSED = ("closed", "Closed")


class ExtenstionsEnum(models.TextChoices):
    pdf = ("pdf", "PDF")
    jpg = ("jpg", "JPEG")
    png = ("png", "PNG")
    webp = ("webp", "WebP")


class StatusEnum(models.TextChoices):
    ANSWERD = ("answered", "Answered")
    UNANSWERED = ("unanswered", "Unanswered")
