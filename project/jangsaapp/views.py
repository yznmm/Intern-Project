from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from .forms import CatForm
from .forms import DogForm 

def main(request):
    return render(request,'jangsaapp/main.html') 

def signup(request): 
    return render(request, 'jangsaapp/signup.html') 

def signin(request):
    return render(request, 'jangsaapp/signin.html')

def cat(request):
    return render(request, 'jangsaapp/cat.html')

def dog(request):
    return render(request, 'jangsaapp/dog.html')

def admincat(request):
    return render(request, 'jangsaapp/admin/admincat.html')

def admindog(request):
    return render(request, 'jangsaapp/admin/admindog.html') 

def add_cat(request):
    context = {}
    form = CatForm(request.POST)   
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "add_cat.html", context) 

def add_dog(request):
    context = {}
    form = DogForm(request.POST)
    if form.is_valid():
        form.save()

    context['form'] = form 
    return render(request, "add_dog.html", context) 




# Create your views here. 
