from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    first_name = None
    last_name = None
    email = models.EmailField('Эл. почта', unique=True)
    is_vip = models.BooleanField('Вип?', default=False)
    name = models.CharField('Имя', max_length=50, blank=True, null=True)
    family = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    otchestvo = models.CharField('Отчество', max_length=50, blank=True, null=True)
    country = models.CharField('Страна', max_length=50, blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    post_code = models.CharField('Индекс', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    passport = models.CharField('Паспортные данные', max_length=255, blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Guest(models.Model):
    email = models.EmailField('Эл. почта', unique=True)
    name = models.CharField('Имя', max_length=50, blank=True, null=True)
    family = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    otchestvo = models.CharField('Отчество', max_length=50, blank=True, null=True)
    country = models.CharField('Страна', max_length=50, blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    post_code = models.CharField('Индекс', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    passport = models.CharField('Паспортные данные', max_length=255, blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, blank=True, null=True)

