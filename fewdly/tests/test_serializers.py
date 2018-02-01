from django.test import TestCase

from fewdly.tests.factories import *
from fewdly.serializers import *


# Create your tests here.
class ReviewerSerializerTestCase(TestCase):

    def test_reviewer_serializer(self):
        reviewer = ReviewerFactory()
        serializer = ReviewerSerializer(reviewer)
        self.assertIsNotNone(serializer.data)


class ReviewSerializerTestCase(TestCase):

    def test_review_serializer(self):
        review = ReviewFactory()
        serializer = ReviewSerializer(review)
        self.assertIsNotNone(serializer.data)


class RestaurantSerializerTestCase(TestCase):

    def test_restaurant_serializer(self):
        restaurant = RestaurantFactory()
        serializer = RestaurantSerializer(restaurant)
        self.assertIsNotNone(serializer.data)

