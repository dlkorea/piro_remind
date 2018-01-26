from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)

from .forms import LoginForm


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            auth_login(request, user)
        next = request.GET.get('next') or request.path
        return redirect(next)

    ctx = {
        'form': form,
    }
    return render(request, 'accounts/login.html', ctx)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect(reverse('accounts:login'))
