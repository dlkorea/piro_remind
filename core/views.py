from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .models import Article
from .forms import ArticleForm, CommentForm


def article_list(request):
    ctx = {
        'article_list': Article.objects.all(),
    }
    return render(request, 'core/article_list.html', ctx)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST or None)
    ctx = {
        'article': article,
        'comment_form': comment_form,
    }
    if request.method == "POST" and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.article = article
        new_comment.save()
        return redirect(article.get_absolute_url())

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


def article_update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST or None, instance=article)

    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }

    return render(request, 'core/article_create.html', ctx)


# 이렇게 하나로 쓸 수도 있다. 상황에 맞게 하면 됨.
def article_create_or_update(request, pk=None):
    if pk is not None:
        article = Article.objects.get(pk=pk)
    else:
        article = None
    form = ArticleForm(request.POST or None, instance=article)

    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }

    return render(request, 'core/article_create.html', ctx)


def article_delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect(reverse('article_list'))
    else:
        return HttpResponse(status=400)
