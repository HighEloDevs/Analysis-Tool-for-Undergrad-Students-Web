from django.urls import path
from . import views


urlpatterns = [
    path("simple_parser", views.simple_parser, name="simple_parser"),
]
