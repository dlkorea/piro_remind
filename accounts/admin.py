from django.contrib import admin

from .models import EmailConfirm, Profile


admin.site.register(EmailConfirm)
admin.site.register(Profile)
