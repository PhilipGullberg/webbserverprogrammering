from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms

tasklist=[]
class NewTaskForm(forms.Form):
    task=forms.CharField(label="Add task")

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasklist.append(task)
            return render(request,'index.html', {
                'tasklist':tasklist,
                'form':form
                
            })
        else:
            return render(request, 'index.html', {
                'form': form
            })
    return render(request, 'index.html', {
        "form":NewTaskForm(),
        "tasklist":tasklist
    })
    


def about(request):
    return render(request,'about.html')

def greet(request, name):
    return render(request, "index.html", {"lista": ['banan', 'apelsin', 'apple', 'godis', 'läsk'],"name":name})