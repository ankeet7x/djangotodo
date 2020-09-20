from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo


# Create your views here.
def todopage(request):
	return render(request, 'home.html', {'datas':ToDo.objects.all()})

def addtodo(request):
	return render(request, 'add.html')
