from django.http.response import HttpResponse
from django.shortcuts import render
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    return render(request, "encyclopedia/page.html", {'title':title, 'entry': util.get_entry(title)} )

def create(request):
    return render(request, "encyclopedia/create.html")

def search(request):
    if request.method=="POST":
        searched=request.POST['q']
        
        error=f'You searched for "{searched}" but that is not an entry we have'
        for entry in util.list_entries():
            if searched.upper()==entry:
                 return render(request, "encyclopedia/page.html", {'title':searched, 'entry': util.get_entry(searched)})
        return render(request, "encyclopedia/page.html", {"error":error})
    else:
        search="Something went wrong"
        return render(request, "encyclopedia/page.html", {"searched":search})

