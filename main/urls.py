from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page),
    path('restaurant/<int:pk>', views.RestaurantsDetail.as_view()),
]