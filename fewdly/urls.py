from django.conf.urls import url

from . import views

app_name = 'fewdly'

urlpatterns = [
    url(r'^reviews/(?P<user_id>[0-9]+)/$', views.Reviews.as_view(), name='review'),
    url(r'^reviews/$', views.Reviews.as_view(), name='review_list'),
    url(r'^restaurantlist/$', views.RestaurantList.as_view(), name='restaurant_list'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$',
        views.RestaurantDetail.as_view(), name='restaurant'),
]
