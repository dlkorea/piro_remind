from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)
from django.core.mail import send_mail

from .models import EmailConfirm
from .forms import (
    AuthForm,
    SignupForm,
)
from .utils import generate_random_string


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


def send_confirm_mail(user):
    try:
        email_confirm = EmailConfirm.objects.get(user=user)
    except EmailConfirm.DoesNotExist:
        email_confirm = EmailConfirm.objects.create(
            user=user,
            key=generate_random_string(length=60),
        )

    url = '{0}{1}?key={2}'.format(
        'http://localhost:8000',
        reverse('accounts:confirm_email'),
        email_confirm.key,
    )
    html = '<p>계속하시려면 아래 링크를 눌러주세요.</p><a href="{0}">인증하기</a>'.format(url)
    send_mail(
        '인증 메일입니다.',
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html,
    )


def login_and_redirect_next(request, user):
    if EmailConfirm.objects.filter(user=user, is_confirmed=True).exists():
        auth_login(request, user)
        next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
        return redirect(next_url)
    else:
        send_confirm_mail(user)
        return redirect(reverse('accounts:email_confirm_sent'))


def email_confirm_sent(request):
    return render(request, 'accounts/email_confirm_sent.html')


def confirm_email(request):
    key = request.GET.get('key')
    email_confirm = get_object_or_404(EmailConfirm, key=key, is_confirmed=False)
    email_confirm.is_confirmed = True
    email_confirm.save()
    return login_and_redirect_next(request, email_confirm.user)



