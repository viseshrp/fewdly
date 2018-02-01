from rest_framework import serializers

from fewdly import models


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviewer
        fields = ('id', 'name',)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('id', 'name',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = ('rating', 'review_text', 'restaurant', 'reviewer', 'created_at', 'id')

