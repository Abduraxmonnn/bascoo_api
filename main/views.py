# Rest-Framework
from rest_framework import viewsets

# Project
from main.models import Product, Contact, EmailMessage
from main.serializers import ProductSerializer, ContactSerializer, EmailMessageSerializer


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
