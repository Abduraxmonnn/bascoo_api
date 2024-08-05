from django.contrib import admin

# Register your models here.
from main.models import Product, Contact, EmailMessage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'created_date', 'last_updated']
    list_display_links = ['id', 'title']
    list_filter = ['is_public']
    search_fields = ['title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_1', 'phone_2', 'email', 'address']
    list_display_links = ['id', 'phone_1', 'phone_2']
    search_fields = ['phone_1', 'phone_2', 'email']


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sender', 'subject', 'created_date']
    list_display_links = ['id', 'name', 'sender']
    search_fields = ['name', 'sender']
