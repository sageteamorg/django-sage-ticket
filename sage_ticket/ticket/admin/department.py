from django.contrib import admin

from sage_ticket.ticket.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    search_fields = ("title",)
    readonly_fields = ("created", "modified")
    ordering = ("title",)
    autocomplete_fields = ("member",)
    fieldsets = (
        (
            None,
            {
                "fields": ("title", "description"),
            },
        ),
        (
            "Members",
            {
                "fields": ("member",),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created", "modified"),
            },
        ),
    )
