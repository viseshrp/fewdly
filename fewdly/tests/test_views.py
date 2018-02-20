from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from fewdly.models import Reviewer, Restaurant, Review
import logging

logger = logging.getLogger(__name__)


class ReviewsListTest(APITestCase):
    """
    Test the review list API
    """

    def setUp(self):
        pass

    def test_list_review(self):
        response = self.client.get(reverse('fewdly:review-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RestaurantListTest(APITestCase):
    """
    Test the restaurant listing API
    """

    def setUp(self):
        pass

    def test_list_restaurant(self):
        response = self.client.get(reverse('fewdly:restaurant-list'),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewCreateTest(APITestCase):
    """
    Test review creation
    """

    def setUp(self):
        self.user = User.objects.create(username='test678')
        self.restaurant = Restaurant.objects.create(
            name='Testaurant', created_at='2018-02-18T21:08:02Z')
        self.client.force_authenticate(user=self.user)  # force auth
        self.data = {
            "rating": 3,
            "review_text": "test",
            "reviewer": 1,
            "restaurant": 1
        }

    def test_can_create_review(self):
        response = self.client.post(reverse('fewdly:create-review'), self.data)
        logger.error(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
