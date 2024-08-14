from django_sage_ticket.ticket.models import Comment
from django.contrib import admin


class ReplayInline(admin.TabularInline):  # or admin.StackedInline
    model = Comment
    fk_name = "replay"
    extra = 1


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "message",
    )
    list_filter = ("status", "issue")
    inlines = [ReplayInline]
