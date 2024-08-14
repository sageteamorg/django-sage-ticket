from django_sage_ticket.ticket.models import Attachment
from django.contrib import admin


@admin.register(Attachment)
class AttachmantAdmin(admin.ModelAdmin):
    list_display = ("name",)

    list_filter = ("name",)
