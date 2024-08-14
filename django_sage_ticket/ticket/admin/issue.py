from django.contrib import admin
from django_sage_ticket.ticket.models import Issue, Attachment, Comment, Department


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1
    fields = ("name", "extensions", "file")
    show_change_link = True


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("title", "user", "message", "state", "is_unread")
    show_change_link = True


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1
    fields = (
        "title",
        "description",
        "member",
    )
    show_change_link = True


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline, CommentInline]
    list_display = ("subject", "state", "created")
    list_filter = ("state", "created")
    search_fields = ("subject", "description")
    ordering = ("-created",)

    fieldsets = (
        (
            None,
            {
                "fields": ("subject", "description", "state"),
            },
        ),
        (
            "Details",
            {
                "fields": ("created", "updated"),
            },
        ),
    )
