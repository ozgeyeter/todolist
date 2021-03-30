from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
from .forms import ListForm

def homepage(request):
    if request.method == "POST":
        form=ListForm[request.POST or None]
        if form.is_valid:
            form.save()
            todo_list = Todos.objects.all()
            return render(request,'homepage.html', {"todo_list" : todo_list})
        else:
            todo_list=Todos.objects.all()
            return render(request,'homepage.html', {"todo_list" : todo_list})
            
            
def about(request):
    return render(request,'about.html')
                

def create(request):
    if request.method == "POST":
        form=ListForm[request.POST or None]
        if form.is_valid:
            form.save()
            todo_list = Todos.objects.all()
            return render(request, 'create.html', {"todo_list" : todo_list})
    else:
        todo_list=Todos.objects.all()
        return render(request, 'create.html' , {"todo_list" : todo_list})
                    
   