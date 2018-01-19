from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='제목',
    )
    content = models.TextField(verbose_name='내용')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}.{1}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'pk': self.pk,
        })
