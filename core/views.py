from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Article
from .forms import ArticleForm


def article_list(request):
    ctx = {
        'article_list': Article.objects.all(),
    }
    return render(request, 'core/article_list.html', ctx)


def article_detail(request, pk):
    ctx = {
        'article': Article.objects.get(pk=pk),
    }
    return render(request, 'core/article_detail.html', ctx)


def article_create(request):
    form = ArticleForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }

    return render(request, 'core/article_create.html', ctx)
