from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from .models import Article, Tag
from .forms import ArticleForm, CommentForm


MAX_COMMENT_COUNT = 100


def article_list(request, tag_pk=None):
    if tag_pk is not None:
        article_list = Article.objects.filter(tag__pk=tag_pk)
        # get_object_or_404 사용하는게 좋음.
        try:
            tag = Tag.objects.get(pk=tag_pk)
        except Tag.DoesNotExist:
            raise Http404('없는 Tag입니다.')
    else:
        article_list = Article.objects.all()
        tag = None

    ctx = {
        'article_list': article_list,
        'tag_list': Tag.objects.all(),
        'tag_selected': tag,
    }
    return render(request, 'core/article_list.html', ctx)


# @login_required
# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     comment_form = CommentForm(
#         request.POST or None,
#         article=article,
#         user=request.user,
#     )
#     if request.method == "POST" and comment_form.is_valid():
#         comment_form.save()
#         return redirect(article.get_absolute_url())

#     ctx = {
#         'article': article,
#         'comment_form': comment_form,
#         'did_like_article': article.liker_set.filter(pk=request.user.pk),
#     }

#     return render(request, 'core/article_detail.html', ctx)


@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_count = article.comment_set.filter(author=request.user).count()
    ctx = {
        'article': article,
        'comment_form': CommentForm(),
        'did_like_article': article.liker_set.filter(pk=request.user.pk),
        'can_write_comment': comment_count < MAX_COMMENT_COUNT,
    }
    return render(request, 'core/article_detail.html', ctx)


@login_required
def comment_create(request, article_pk):
    if request.POST:
        article = Article.objects.get(pk=article_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()

            return render(request, 'core/comment.html', {
                'comment': comment,
            })

    return HttpResponse(status=405)


@login_required
def article_create(request):
    form = ArticleForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }

    return render(request, 'core/article_create.html', ctx)


@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)

    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())

    ctx = {
        'form': form,
    }

    return render(request, 'core/article_create.html', ctx)


# 이렇게 하나로 쓸 수도 있다. 상황에 맞게 하면 됨.
@login_required
def article_create_or_update(request, pk=None):
    if pk is not None:
        article = get_object_or_404(Article, pk=pk)
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


@login_required
def article_delete(request, pk):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect(reverse('core:article_list'))
    else:
        return HttpResponse(status=400)


@login_required
def article_like(request, pk):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=pk)

        if request.user.liked_article_set.filter(pk=pk).exists():
            article.liker_set.remove(request.user)
        else:
            article.liker_set.add(request.user)

        ctx = {
            'did_like_article': article.liker_set.filter(pk=request.user.pk).exists(),
            'article': article,
        }
        return render(request, 'core/article_like_button.html', ctx)

    else:
        return HttpResponse(status=400)
