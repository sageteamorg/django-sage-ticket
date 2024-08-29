from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sage_ticket.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    readonly_fields = ("created_at", "modified_at")
    ordering = ("title",)
    autocomplete_fields = ("member",)
    fieldsets = (
        (
            None,
            {
                "fields": ("title", "description"),
                "description": _(
                    "Fields related to the department, including its title and description."
                ),
            },
        ),
        (
            _("Members"),
            {
                "fields": ("member",),
                "description": _(
                    "Field for the members associated with this department."
                ),
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": ("created_at", "modified_at"),
                "description": _(
                    "Auto-generated timestamps indicating when the department was created_at and last modified_at."
                ),
            },
        ),
    )
