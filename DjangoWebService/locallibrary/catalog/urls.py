from django.urls import path
from django.urls import include, re_path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('message', views.message, name='message'),
  path('books/',  views.BookListView.as_view(), name='books'),
  path('authors/', views.AuthorsListView.as_view(), name='authors'),
]