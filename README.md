# Hello! Welcome to Fewdly, a Parade project

## Overview
This project is designed to go over some basic Django and Django Rest Framework skills.
Fewdly is a simple food review app (think Yelp). We are about to pitch our idea
to some high-profile VCs, but we need a build a proof-of-concept first.
Here is what needs to be done:

## Getting started
We've created a Django app for you called fewdly. We've provided the standard
Django app structure, but we've left everything else empty for you
to fill in.

To get started, you can run

`pip install -r requirements/base.txt`

`pip install -r requirements/test.txt`

This will install Django, Django Rest Framework, and some testing libraries.

If you run

`python manage.py runserver`

You should see the Django successful installation page.

## Models
Let's get started with some models. We need to represent our data somehow.
Think about what might be needed in a food app. Here are some ideas:
- Reviewers
- Reviews
- Restaurants

## Serializers
This is optional. Feel free to create some serializers for your models using Django Rest Framework.
You are also welcome to just live with the built-in Django serializers.

## API & Views
How are people supposed to see their reviews? We need to expose this via an API.
Fill out `urls.py` and `views.py` so that we can perform the basic CRUD
operations on all our models. Django Rest Framework will save you a lot of time here.

As for the actual view templates, don't go too crazy. Feel free to use the DRF
API views for something quick and simple.


## Permissions
Should everyone be able to post reviews? How about adding restaurants? Let's add
some permission restrictions to our API. Think about what might make sense
and go for it.

## Testing
Let's test our API! Add some tests :)

## Conclusion
You're done! Fewdly is on its way to becoming the next big thing :)

