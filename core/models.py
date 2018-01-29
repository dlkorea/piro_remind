from django.db import models
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='제목',
    )
    content = models.TextField(verbose_name='내용')

    liker_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_article_set',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return '{0}.{1}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('core:article_detail', kwargs={
            'pk': self.pk,
        })


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
