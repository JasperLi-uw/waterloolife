from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_newest_threads, name='get_newest_threads'),
    path('<int:thread_pk>', views.thread_detail, name="thread_detail"),
    path('type/<int:thread_type_pk>', views.threads_with_type, name="threads_with_type"),
]
