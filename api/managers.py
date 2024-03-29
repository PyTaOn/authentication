from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class GerenciadorUsuario(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser):
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff, is_superuser=is_superuser
        )
        user.set_password(password)
        return user

    def create_user(self, email, password):
        user = self._create_user(email, password, is_staff=False, is_superuser=False)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self._create_user(email, password, is_staff=True, is_superuser=True)
        user.save(using=self._db)

        return user
