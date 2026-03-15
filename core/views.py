from django.shortcuts import render

def index(request):
    context = {
        "key": "Django"
    }
    return render(request, 'index.html', context)
