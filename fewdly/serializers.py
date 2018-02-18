from rest_framework import serializers
from fewdly.models import Review, Reviewer, Restaurant
from django.conf import settings


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')
