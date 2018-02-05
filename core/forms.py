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

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     self.article = kwargs.pop('article')
    #     super().__init__(*args, **kwargs)

    # def clean(self):
    #     comment_count = self.user.comment_set.filter(article=self.article).count()
    #     if comment_count >= 5:
    #         raise forms.ValidationError('댓글은 5회만 남기실 수 있습니다.')

    # def save(self):
    #     comment = super().save(commit=False)
    #     comment.article = self.article
    #     comment.author = self.user
    #     comment.save()
    #     return comment
