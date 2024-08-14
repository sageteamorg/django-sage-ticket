from django.contrib import admin
from django_sage_ticket.ticket.models import Issue, Department


class DepartmentInline(admin.StackedInline):
    model = Department


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "message",
    )
    list_filter = ("severity", "state")
    search_fields = ("name", "subject")
    # inlines = [DepartmentInline]
