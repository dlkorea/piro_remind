from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('tag/<int:tag_pk>', views.article_list, name='article_list_by_tag'),
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('<int:pk>/update/', views.article_update, name='article_update'),
    path('<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('<int:pk>/like/', views.article_like, name='article_like'),
    path('comment/create_ajax/', views.comment_create_ajax, name='comment_create_ajax'),
]
