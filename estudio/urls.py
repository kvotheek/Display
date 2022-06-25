
from django.urls import path
from .views import estudio1, answer

urlpatterns= [
    path('', estudio1, name='estudio'),
    path('answer/', answer, name='respuesta_1')
]
