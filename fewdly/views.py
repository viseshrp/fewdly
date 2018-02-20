from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.reverse import reverse
from .models import Review, Reviewer, Restaurant
from .serializers import ReviewSerializer, ReviewerSerializer, RestaurantSerializer
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'restaurants': reverse('fewdly:restaurant-list', request=request),
            'reviews': reverse('fewdly:review-list', request=request)
        }
    )


@api_view(['GET'])
@authentication_classes((authentication.BasicAuthentication, authentication.SessionAuthentication))
@permission_classes((permissions.IsAuthenticated,))
def get_user_review(request, user_id):
    # get review per user
    try:
        reviewer = Reviewer.objects.get(pk=user_id)
    except Reviewer.DoesNotExist:
        logger.error("Reviewer obj not found!")
        return Response(status=status.HTTP_404_NOT_FOUND)

    review_list = reviewer.review_set.all()

    serializer = ReviewSerializer(review_list, many=True)
    return Response(serializer.data)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a restaurant
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewList(generics.ListAPIView):
    """
    Retrieve list of reviews.
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.AllowAny,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    """
    Create review.
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RestaurantList(generics.ListAPIView):
    """
    Retrieve list of restaurants.
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.AllowAny,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantCreate(generics.CreateAPIView):
    """
    Create restaurants.
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAdminUser,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a restaurant
    """
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.SessionAuthentication)
    # only allow authenticated users to see reviews
    permission_classes = (permissions.IsAdminUser,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
