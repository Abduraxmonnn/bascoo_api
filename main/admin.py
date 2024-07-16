from django.contrib import admin

# Register your models here.
from main.models import Product, Contact, EmailMessage


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(EmailMessage)
