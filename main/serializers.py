# Rest-Framework
import asyncio

from rest_framework import serializers

# Project
from main.models import Product, Contact, EmailMessage
from main.telegram_bot import send_msg_to_group


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = '__all__'

    def create(self, validated_data):
        created = EmailMessage.objects.create(**validated_data)
        asyncio.run(send_msg_to_group(validated_data, created))
        return created
