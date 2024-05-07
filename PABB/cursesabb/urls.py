from django.urls import path
from cursesabb import views  

urlpatterns = [
    
    path('',views.home),
    path('cursos/',views.cursos),
    path('progreso/',views.mostrar_progreso)
    
]