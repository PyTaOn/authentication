from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import GerenciadorUsuario
import uuid
# Create your models here.


class Usuario(AbstractBaseUser):
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = models.CharField('senha', max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = GerenciadorUsuario()

    def __str__(self):
        return self.email