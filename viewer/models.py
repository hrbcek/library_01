from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, DateField, ForeignKey, DO_NOTHING, SET_NULL, ManyToManyField, \
    DateTimeField, TextField, BooleanField
from django_resized import ResizedImageField
from django.utils import timezone


# Create your models here.

class Book(Model):
    title = CharField(max_length=128)
    author = CharField(max_length=64)
    images = ManyToManyField("Image", blank=True, related_name="books")
    categories = ManyToManyField("Category", blank=True, related_name="books")

    # owner = ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_borrowed = BooleanField(default=False)
    borrowed_date = DateTimeField(null=True, blank=True, default=timezone.now)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"


class Person(Model):
    op = CharField(max_length=16)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    birth_date = DateField(null=True, blank=True)





class Image(Model):
    # url = CharField(max_length=128, null=False, blank=False)
    image = ResizedImageField(size=[500,500], upload_to='static/images/', default=None, null=False,
                       blank=False)
    description = TextField()

    def __str__(self):
        return f"{self.description[:50]}"


class Category(Model):
    name = CharField(max_length=64)
    parent_category = ForeignKey("Category", on_delete=SET_NULL, null=True, blank=True, related_name="categories")


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

class BorrowedBook(Model):
    # user = ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = ForeignKey('Book', on_delete=models.CASCADE)
    borrow_date = DateTimeField(auto_now_add=True)
    return_date = DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"








