from django.contrib import admin
from django.urls import path, include

# Rest-Framework
from rest_framework import routers

# Project
from main.views import ProductViewSet, ContactViewSet, EmailMessageViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'email/message/', EmailMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
