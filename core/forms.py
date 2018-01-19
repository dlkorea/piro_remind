from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if (title is not None) and ('woo' in title):
            return title
        else:
            raise forms.ValidationError('woo가 필요합니다.')
