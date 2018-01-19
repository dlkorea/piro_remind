from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30, label='제목')
    content = forms.CharField(label='내용')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if (title is not None) and ('woo' in title):
            return title
        else:
            raise forms.ValidationError('woo가 필요합니다.')
