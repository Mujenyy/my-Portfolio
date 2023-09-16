from django.shortcuts import render

def home(request): #request is argument of home
    return render(request, 'home.html', {})
