from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('<int:pk>/update/', views.article_update, name='article_update'),
    path('<int:pk>/delete/', views.article_delete, name='article_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
