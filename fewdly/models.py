from django.db import models

# Create some models here!


class Reviewer(models.Model):
    name = models.CharField(max_length=100)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)


class Review(models.Model):
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    review_text = models.CharField(max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
