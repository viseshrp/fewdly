from django.test import Client
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from fewdly.tests.factories import *
from fewdly.serializers import *

import json


class ReviewerViewSetTestCase(APITestCase):

    def test_get(self):
        reviewer = ReviewerFactory()
        reviewer.save()

        response = self.client.get('/reviewers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        reviewer = ReviewerFactory()
        s = ReviewerSerializer(reviewer)
        response = self.client.post('/reviewers/', s.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReviewViewSetTestCase(APITestCase):

    def test_get(self):
        review = ReviewFactory()
        review.save()

        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_unauthenticated(self):
        review = ReviewFactory()
        review.save()
        s = ReviewSerializer(review)
        response = self.client.post('/reviews/', s.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_authenticated(self):
        review = ReviewFactory()
        review.save()
        s = ReviewSerializer(review)
        user = User.objects.create_user(username='test', password='test')
        user.save()
        c = Client()
        c.login(username='test', password='test')
        response = c.post('/reviews/', s.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RestaurantViewSetTestCase(APITestCase):

    def test_get(self):
        restaurant = RestaurantFactory()
        restaurant.save()

        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_unauthenticated(self):
        restaurant = RestaurantFactory()
        s = RestaurantSerializer(restaurant)
        response = self.client.post('/restaurants/', s.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_authenticated(self):
        restaurant = RestaurantFactory()
        s = RestaurantSerializer(restaurant)
        user = User.objects.create_superuser(username='test', email='test@test.com', password='test')
        user.save()
        c = Client()
        c.login(username='test', password='test')
        response = c.post('/restaurants/', s.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
