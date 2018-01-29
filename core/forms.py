from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('liker_set', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'author', )
