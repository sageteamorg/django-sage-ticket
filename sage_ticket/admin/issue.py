from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sage_ticket.models import Attachment, Comment, Department, Issue


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1
    fields = ("name", "extensions", "file")
    show_change_link = True


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("title", "user", "message", "is_unread")
    show_change_link = True


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1
    fields = ("title", "description", "member")
    show_change_link = True


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline, CommentInline]
    list_display = ("subject", "state", "created_at")
    list_filter = ("state", "created_at")
    search_fields = ("subject", "message")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "modified_at")
    fieldsets = (
        (
            None,
            {
                "fields": ("subject", "message", "state", "department", "raised_by"),
                "description": _(
                    "Fields related to the issue, including the subject, description, and current state."
                ),
            },
        ),
        (
            _("Details"),
            {
                "fields": ("created_at", "modified_at"),
                "description": _(
                    "Auto-generated timestamps indicating when the issue was created_at and last updated."
                ),
            },
        ),
    )
