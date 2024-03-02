from django.shortcuts import render

def index(request):
    return render(request, 'simple_app/index.html')