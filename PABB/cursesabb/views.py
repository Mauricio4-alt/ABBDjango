from django.shortcuts import render
from django.http import HttpResponse as Response
# Create your views here.
def home(request):
    doc ='''<H1>Bienvenido a nuestra escuela sientete libre de explorar nuestros cursos</H1>
    <p>
    <ul>
        <li><a href="http://127.0.0.1:8000/cursos">Cursos</a></li>
        <li><a href="http://127.0.0.1:8000/progreso">progreso</a></li>
        
        
    </ul>
    </p>    
    
    
    '''
    return Response(doc)
def cursos(request):
    doc = '''
    <h1>
    Curso de html basico
    </h1>
    <p>
    En este curso conocerás los fundamentos básicos que conforman una pagina web 
    Vas a crear tu primer blog informativo
    y entenderás como utilizar cada una de las sentencias HTML y a adaptarlas 
    para cada navegador
    </p>
    
    '''
    return Response(doc)
def mostrar_progreso(request):
    p = 0
    doc =f'''
    <p>
    TU progreso es de {p} porciento en curso de html 
    </p>
    
    '''
    return Response(doc)
