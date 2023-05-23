from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
import random



lists=util.list_entries()


markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,title):
    
    if util.get_entry(title) == None:
         return render(request, "encyclopedia/error.html", {
            'message': f'Error: [{title}] - Entry not found'
        })
    else:     
        return render(request, "encyclopedia/entry.html", {
            'title':title,
            'entry': markdowner.convert(util.get_entry(title)) 
        })
        
        
def search(request):
    if request.method == 'POST':
        entry_search = request.POST['q']
        entries = util.list_entries()
        match_entries = [entry for entry in entries if entry_search.lower()in entry.lower()]
        if util.get_entry(entry_search) is not None:
            return render(request, "encyclopedia/entry.html", {
                'title':entry_search,
                'entry': markdowner.convert(util.get_entry(entry_search)) 
            })
        elif match_entries:
            return render(request, 'encyclopedia/search.html', {
                'entries' : match_entries,
                'entry_search' : entry_search
            })
        else:
            return render(request, "encyclopedia/error.html", {
                    'message': f'No results found for : {entry_search}'
            })
    

# function to make new entry it should take title and content and use save_entry(title, content)


def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                'message': f'Error: [{title}] - Entry already exists'
            })
        else:
            util.save_entry(title,content)
            return render(request, "encyclopedia/entry.html", {
                'title':title,
                'entry': markdowner.convert(util.get_entry(title)) 
            })
    else:
        return render(request, "encyclopedia/new_entry.html")        
    
    
def edit_entry(request, title):
    if request.method == 'GET':
        entry = util.get_entry(title)
        if entry is None:
            return render(request, "encyclopedia/error.html", {
                'message': f'Error: [{title}] - Entry not found'
            })
        else:
            return render(request, "encyclopedia/edit_entry.html", {
                'title': title,
                'entry': entry
            })
    elif request.method == 'POST':
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('entry', title=title)
    
    
def random_entry(request):
    title = random.choice(lists)
    return render(request, "encyclopedia/entry.html", {
            'title':title,
            'entry': markdowner.convert(util.get_entry(title)) 
        })    