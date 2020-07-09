from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('add/', views.PostClass.as_view(), name='add'),
    path('save/', views.ClassSaveNews.as_view(), name='save'),
    path('email/', views.email_view, name='email'),
    path('process', views.process, name='pro'),
]