from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should br provided"))

        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)

        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super should have is_staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("superuser should have is_super as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))

        return self.create_user(email, password, **extra_fields)




class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER = [(MALE, MALE), (FEMALE, FEMALE), (OTHER, OTHER)]

    username=None
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    address = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.email


class Artist(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER = [(MALE, MALE), (FEMALE, FEMALE), (OTHER, OTHER)]

    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=30, choices=GENDER)
    address = models.CharField(max_length=255)
    first_release_year = models.DateField()
    no_of_albums_released = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name


class Music(models.Model):
    MB = 'mb'
    COUNTRY = 'country'
    CLASSIC = 'classic'
    ROCK = 'rock'
    JAZZ = 'jazz'
    GENRE = [(MB, MB), (COUNTRY, COUNTRY), (CLASSIC, CLASSIC), (ROCK, ROCK),
             (JAZZ, JAZZ)]
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.artist.name + " " + self.title
