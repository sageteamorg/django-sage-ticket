from django.contrib import admin

from sage_ticket.ticket.models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("name", "issue", "extensions", "file", "created")
    list_filter = ("extensions", "created")
    search_fields = ("name", "issue__title")
    readonly_fields = ("created", "modified")
    raw_id_fields = ("issue",)
    ordering = ("-created",)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "issue", "extensions", "file"),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created", "modified"),
            },
        ),
    )
