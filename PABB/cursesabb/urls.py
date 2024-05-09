from django.urls import path
from cursesabb import views  

urlpatterns = [
    
    path('home',views.home),
    path('login/',views.login),
    path('cursos/',views.cursos)
    
]