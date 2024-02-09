from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateForm
# Create your views here.
def index(request):
    title = "Django Course!!"
    return render(request, 'index.html', {'title': title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    return render(request, 'tasks.html')

def hello(request, username):
    return HttpResponse(f"Hello, {username}. You're at the myapp index.")

def form(request):
    if request.method == 'GET':
        return render(request, 'form.html', {'form': CreateForm()})
    else:
        Project.objects.create(name=request.POST['name'], 
                               description=request.POST['description'], 
                               done=False)
        print(request.POST)
        return redirect('projects') 