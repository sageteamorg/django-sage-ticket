from django.contrib import admin
from django_sage_ticket.ticket.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "issue", "status", "is_unread", "created")
    list_filter = ("status", "is_unread", "created")
    search_fields = ("title", "user__username", "issue__title")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "user", "issue", "message", "status", "is_unread"),
            },
        ),
        (
            "Reply",
            {
                "fields": ("replay",),
                "classes": ("collapse",),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created", "modified"),
            },
        ),
    )
