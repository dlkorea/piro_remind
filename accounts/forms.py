from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "아이디 또는 패스워드가 틀렸습니다.",
        'inactive': "탈퇴한 계정입니다.",
    }
