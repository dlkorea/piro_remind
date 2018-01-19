from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Article


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
    ctx = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            article = Article.objects.create(
                title=title,
                content=content,
            )
            url = reverse('article_detail', kwargs={
                'pk': article.pk,
            })
            return redirect(url)
        else:
            error_msg = {}
            if not title:
                error_msg.update({'title': '제목을 입력해주세요.'})
            if not content:
                error_msg.update({'content': '내용을 입력해주세요.'})
            ctx.update({'error': error_msg, })

    return render(request, 'core/article_create.html', ctx)
