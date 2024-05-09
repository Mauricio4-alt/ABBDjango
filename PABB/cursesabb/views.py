from django.shortcuts import render
from django.http import HttpResponse as Response
# Create your views here.
def home(request):
   
    return render(request,'cursesabb/home.html')
def login(request):
    
    return render(request,'cursesabb/login.html')
def cursos(request,):
   
    return render(request,'cursesabb/cursos.html')
