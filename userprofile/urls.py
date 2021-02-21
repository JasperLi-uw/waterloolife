from django.urls import path
from . import views

urlpatterns = [
	path('', views.nothing, name="nothing"),
	path('edit/<int:id>/', views.profile_edit, name='edit'),
]