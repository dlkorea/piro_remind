from django.db import models
from django.conf import settings


class EmailConfirm(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='email_confirm',
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    birth_day = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_profile_image.jpg'
        return image_url
