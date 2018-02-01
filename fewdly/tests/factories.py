from fewdly.models import *
from faker import Faker

import factory

fake = Faker()


class ReviewerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reviewer

    name = factory.LazyAttribute(lambda n: fake.first_name())


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.LazyAttribute(lambda n: fake.first_name() + "'s Diner")


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    rating = 5
    review_text = "Awesome!"
    restaurant = factory.SubFactory(RestaurantFactory)
    reviewer = factory.SubFactory(ReviewerFactory)
