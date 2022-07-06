from django.contrib import admin

from .models import EmailConfirmationRequests, PasswordChangeRequests

admin.site.register(EmailConfirmationRequests)
admin.site.register(PasswordChangeRequests)
