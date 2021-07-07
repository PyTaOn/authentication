from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class GerenciadorUsuario(BaseUserManager):
    def _create_user(self, email, senha, is_staff, is_superuser):
        email = self.normalize_email(email)
        user = self.model(
            email, is_staff=is_staff, is_superuser=is_superuser, data_cadastro=timezone.localtime()
        )
        user.set_password(senha)
        return user

    def create_user(self, email, senha):
        user = self._create_user(email, senha, is_staff=False, is_superuser=False)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, senha):
        user = self._create_user(email, senha, is_staff=True, is_superuser=True)
        user.save(using=self._db)

        return user
