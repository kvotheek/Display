from django.shortcuts import render
from .models import alternativas, imagen_patologica
"""
def home(request):
    
    return render(request, 'home.html')

"""
def home(request):
    return render(request, 'home.html')

def estudio1(request):
    respuestas= alternativas.objects.all()
    imagenes= imagen_patologica.objects.all()
    return render(request, 'estudio.html',{'respuestas': respuestas, 'imagenes':imagenes})

def answer(request):
    respuestas= alternativas.objects.all()
    imagenes= imagen_patologica.objects.all()
    return render(request,'respuesta_1.html', {'respuestas': respuestas, 'imagenes':imagenes})