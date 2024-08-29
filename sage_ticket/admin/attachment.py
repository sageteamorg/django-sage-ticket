from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sage_ticket.models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("name", "issue", "extensions", "file", "created_at")
    list_filter = ("extensions", "created_at")
    search_fields = ("name", "issue__title")
    readonly_fields = ("created_at", "modified_at")
    raw_id_fields = ("issue",)
    ordering = ("-created_at",)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "issue", "extensions", "file"),
                "description": _(
                    "Fields related to the attachment, including its name, associated issue, file extension, and the file itself."
                ),
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": ("created_at", "modified_at"),
                "description": _(
                    "Auto-generated timestamps indicating when the attachment was created_at and last modified_at."
                ),
            },
        ),
    )
