from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import GerenciadorUsuario
import uuid
from django.utils import timezone

# Create your models here.


class Usuario(AbstractBaseUser):
    email = models.EmailField("Email", max_length=255, unique=True)
    senha = models.CharField("senha", max_length=20)
    data_cadastro = models.DateTimeField("Data de Cadastro", default=timezone.localtime())
    pessoa_fisica = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = GerenciadorUsuario()

    def __str__(self):
        return self.email
