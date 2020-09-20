from django.urls import path
from . import views


urlpatterns = [
	path('todos/', views.index, name = 'todo-page')
]