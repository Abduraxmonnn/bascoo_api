# Rest-Framework
from django.contrib.auth import authenticate
from rest_framework import viewsets, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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


class LoginAPIView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'username': token.user.username,
                'status': 'successfully',
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
