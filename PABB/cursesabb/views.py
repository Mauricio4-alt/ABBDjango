from django.shortcuts import render
from django.http import HttpResponse as Response
# Create your views here.
def home(request):
   
    return render(request,'cursesabb/pagina.html')
def cursos(request):
    
    return render(request,'cursesabb/Templates/login/cursos.html')
def mostrar_progreso(request,):
   
    return render(request,'cursesabb/Templates/login/progreso')
