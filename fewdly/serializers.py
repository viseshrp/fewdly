from rest_framework import serializers
from fewdly.models import Review, Reviewer, Restaurant


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
        model = Reviewer
        fields = '__all__'
