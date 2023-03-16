from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page),
    path('restaurant/<int:pk>', views.RestaurantsDetail.as_view()),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('registration/', views.user_registration, name="registration"),
]