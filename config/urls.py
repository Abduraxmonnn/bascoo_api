# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Rest-Framework
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Project
from main.views import ProductViewSet, ContactViewSet, EmailMessageViewSet, LoginAPIView
from config.yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'email/message', EmailMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', obtain_auth_token, name='auth'),
    path('login/', LoginAPIView.as_view()),

    path('', include('admin_soft.urls')),
    path('', include(router.urls))
]

urlpatterns += doc_urls

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


