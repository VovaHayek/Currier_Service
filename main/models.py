from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='user_images/')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

#Restaurant Tags
class Tags(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

#Restaurants
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    restaurant_image = models.ImageField(upload_to='restaurant_images/', blank=False)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.restaurant_name

#Restaurant Dishes
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, blank=False)
    dish_name = models.CharField(max_length=100)
    dish_desc = models.TextField(blank=True)
    price = models.IntegerField(default=0, blank=False)
    dish_image = models.ImageField(upload_to='dishes/')

    def __str__(self):
        return self.dish_name

#Orders
class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    dishes = models.ManyToManyField(Menu, blank=False)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant.restaurant_name
