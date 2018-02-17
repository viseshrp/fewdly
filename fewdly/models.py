from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import logging

logger = logging.getLogger(__name__)


class Reviewer(AbstractUser):
    phone = models.CharField(unique=True, max_length=10, default='')
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    name = models.CharField(unique=True, max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    created_at = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review_text = models.TextField(max_length=4000, null=True)

    def __str__(self):
        return self.rating

    class Meta:
        ordering = ['rating']
