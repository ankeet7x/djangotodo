from django.urls import path
from . import views



urlpatterns = [
	path('', views.todopage, name = 'todo-page'),
	path('addtodo/', views.addtodo, name = 'add-page'),
	path('delete/<id>', views.delete, name = 'delete')
]