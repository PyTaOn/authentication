from django.contrib import admin
from django.urls import path

from api import viewsets

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


urlpatterns = [
    path('authenticate/', views.obtain_auth_token),
    path('create-user/', viewsets.CustomUserViewSet.as_view({'post': 'create'})),
    path('admin/', admin.site.urls),
]
