from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("user/", views.UserView.as_view()),
    path("send_email_confirmation/", views.send_email_confirmation),
    path("confirm_email/", views.confirm_email),
]
