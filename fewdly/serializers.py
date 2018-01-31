from rest_framework import serializers

from fewdly import models


class ReviewerSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.Reviewer
        fields = ('name',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('rating', 'review_text', 'restaurant', 'reviewer', 'created_at',)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('name',)
