from django.urls import path
from pages import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("guitar-lessons/", views.GuitarPageView.as_view(), name="guitar-lessons")
]