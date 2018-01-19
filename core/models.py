from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='제목',
    )
    content = models.TextField(verbose_name='내용')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
