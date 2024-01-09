from django.contrib import admin
from myapp.models import Message


@admin.register(Message)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date', 'is_processed')
    search_fields = ['name', 'email', 'subject']
    list_filter = ['is_processed']
    readonly_fields = ['date']
