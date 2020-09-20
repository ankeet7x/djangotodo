from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
import json
# from rest_framework import serializers
# from django.core import serializers
# from .forms import ToDoForm


# Create your views here.
def todopage(request):
	datas = ToDo.objects.all()
	# json_data = serializers.serialize("json",datas)
	# datas = json.loads(json_data)
	return render(request, 'home.html', {'datas': datas})

def addtodo(request):
	return render(request, 'add.html')
