from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('confirm/', views.confirm_email, name='confirm_email'),
    path('confirm/sent/', views.email_confirm_sent, name='email_confirm_sent'),

    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]
