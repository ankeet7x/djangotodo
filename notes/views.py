from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import ToDoForm



# Create your views here.
def todopage(request):
	datas = ToDo.objects.all()
	# json_data = serializers.serialize("json",datas)
	# datas = json.loads(json_data)
	return render(request, 'home.html', {'datas': datas})



def addtodo(request):
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			data = form.save(commit= False)
			data.save()
			return redirect('todo-page',)

	else:
		form = ToDoForm()
		return render(request, 'add.html', {'form': form})

	# form = ToDoForm()	
	# return render(request, 'add.html', {'form': form})

