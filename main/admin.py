from django.contrib import admin

# Register your models here.
from main.models import Product, Contact, EmailMessage


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sender', 'subject', 'created_date']
    list_display_links = ['id', 'name', 'sender']
    search_fields = ['name', 'sender']


admin.site.register(Product)
admin.site.register(Contact)
