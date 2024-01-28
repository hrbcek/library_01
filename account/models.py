from django.apps import AppConfig
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField, CharField, DateField, TextField, OneToOneField, CASCADE, ManyToManyField, Model

from viewer.models import BorrowedBook


class CustomUser(AbstractUser):

    title = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=[
        ('M', 'Muž'),
        ('F', 'Žena'),
        ('O', 'Ostatní'),
    ])
    avatar = models.ImageField(upload_to="avatars/", default='avatars/default_avatar.webp')
    birth_date = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    op = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.email


class Profile(Model):
    user = OneToOneField(CustomUser, on_delete=CASCADE, related_name='profile')
    username = CharField(max_length=150, unique=True)
    title = CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'other_required_field']
    GENDER_CHOICES = [
        ('M', 'Muž'),
        ('F', 'Žena'),
        ('O', 'Ostatní'),
    ]
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar = ImageField(upload_to="avatars/", default='avatars/default_avatar.webp')
    birth_date = DateField(null=True, blank=True)
    mobile_number = CharField(max_length=15, blank=True)
    address = TextField(blank=True)
    op = CharField(max_length=16, blank=True)

    borrowed_books = ManyToManyField(BorrowedBook, blank=True)

    def __str__(self):
        return self.user.email

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'


