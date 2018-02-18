from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.decorators import permission_classes
from .models import Review, Reviewer, Restaurant
from .serializers import ReviewSerializer, ReviewerSerializer, RestaurantSerializer
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


class Reviews(APIView):
    """
    List all reviews per user, or create a review
    """
    # setting auth per view. Set globally in settings.py
    authentication_classes = (authentication.BasicAuthentication,)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_id=None):
        if user_id is None:
            review_list = Review.objects.all()
        else:
            try:
                reviewer = Reviewer.objects.get(pk=user_id)
            except Reviewer.DoesNotExist:
                logger.error("Reviewer obj not found!")
                return Response(status=status.HTTP_404_NOT_FOUND)

            review_list = reviewer.review_set.all()

        serializer = ReviewSerializer(review_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantList(APIView):
    """
    Retrieve list of restaurants
    """

    authentication_classes = (authentication.BasicAuthentication,)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        restaurant_list = Restaurant.objects.all()
        # logger.error(review_list)
        serializer = RestaurantSerializer(restaurant_list, many=True)

        return Response(serializer.data)


class RestaurantDetail(APIView):

    authentication_classes = (authentication.BasicAuthentication,)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
