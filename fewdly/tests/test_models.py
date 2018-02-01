from django.test import TestCase, RequestFactory

from fewdly.tests.factories import *


class ReviewerTestCase(TestCase):

    def test_create_review(self):
        reviewer = ReviewFactory()
        self.assertIsNotNone(reviewer)


class ReviewTestCase(TestCase):

    def test_create_review(self):
        review = ReviewFactory()
        self.assertIsNotNone(review)


class RestaurantTestCase(TestCase):

    def test_create_review(self):
        restaurant = RestaurantFactory()
        self.assertIsNotNone(restaurant)

