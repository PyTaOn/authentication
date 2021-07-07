from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


class GerenciadorUsuario(BaseUserManager):
    def create_user(self, email, senha):
        if not email and not senha:
            raise ValueError('Todos os campos devem ser preenchido.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(senha)
        user.save(using=self._db)

        return user
