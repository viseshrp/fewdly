from django.conf.urls import url

from . import views

app_name = 'fewdly'

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^reviews/$', views.ReviewList.as_view(), name='review-list'),
    url(r'^create-review/$', views.ReviewCreate.as_view(), name='create-review'),
    url(r'^review/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view(), name='review'),
    url(r'^user-reviews/(?P<user_id>[0-9]+)/$', views.get_user_review, name='user-review'),
    url(r'^restaurants/$', views.RestaurantList.as_view(), name='restaurant-list'),
    url(r'^create-restaurant/$', views.RestaurantCreate.as_view(), name='create-restaurant'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$',
        views.RestaurantDetail.as_view(), name='restaurant'),
    url(r'^get-average-review/(?P<restaurant_id>[0-9]+)/$',
        views.get_average_review, name='get-average-review'),
]
