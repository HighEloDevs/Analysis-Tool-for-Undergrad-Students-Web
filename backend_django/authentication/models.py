from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class EmailConfirmationRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
    expires_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(hours=12)
    )


class PasswordChangeRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    expires_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(hours=12)
    )
