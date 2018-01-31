from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)


class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "아이디 또는 패스워드가 틀렸습니다.",
        'inactive': "탈퇴한 계정입니다.",
    }


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': '패스워드가 일치하지 않습니다.',
    }

    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is not None and email.split('@')[1] != 'snu.ac.kr':
            raise forms.ValidationError('snu 이메일만 가입이 가능합니다.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
