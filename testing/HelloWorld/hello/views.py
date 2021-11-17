from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse


tasks=[]
class NewTaskForm(forms.Form):
    
    task = forms.CharField(label="Add task")
# Create your views here.
def cool(request):
    return render(request, "index.html")

def hello(request):
    return HttpResponse("Hello Philip")

def about(request):
    return render(request,'about.html')

def greet(request,name):
    return render(request, "about.html", {"lista": ['banan', 'apelsin', 'apple', 'godis', 'läsk'], "name":name})

def add(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            return render(request,'task.html',{
                'tasks':tasks,
                'form':NewTaskForm()
            })
        else:
            return render(request, 'task.html',{
                "form":form
            })
    return render(request, 'task.html',{
        "form":NewTaskForm(),
        "tasks":tasks,
    })
