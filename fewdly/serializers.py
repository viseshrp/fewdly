from rest_framework import serializers
from fewdly.models import Review, Reviewer, Restaurant
from django.conf import settings
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviewer
        fields = ('phone', 'state', 'zip_code')
