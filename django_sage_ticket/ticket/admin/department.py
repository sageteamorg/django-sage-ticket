from django_sage_ticket.ticket.models import Department
from django.contrib import admin


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("name", "title")
