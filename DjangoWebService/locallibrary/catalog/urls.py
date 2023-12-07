from django.urls import path
from django.urls import include, re_path
from .models import Thread
from . import views
from .views import ThreadDetailView
from .views import show_thread
#создать url пути к существующим вещам через клики в thread_list



urlpatterns = [
  path('', views.index, name='index'),
  path('threads/',  views.ThreadListView.as_view(), name='threads'),
 # path("threads/<slug:thread_detail>/", ThreadDetailView.as_view(), name="thread_detail"),
  path('threads/<slug:thread_slug>/', show_thread, name='thread'),
]