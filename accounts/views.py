from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)

from .forms import AuthForm, SignupForm


def login(request):
    form = AuthForm(request, request.POST or None)
    if request.method == "POST" and form.is_valid():
        return login_and_redirect_next(request, form.get_user())

    ctx = {
        'form': form,
    }
    return render(request, 'accounts/login.html', ctx)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect(reverse('accounts:login'))


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return login_and_redirect_next(request, user)
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', ctx)


def login_and_redirect_next(request, user):
    auth_login(request, user)
    next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
    return redirect(next_url)











