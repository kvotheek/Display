from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields import CharField, URLField, PositiveSmallIntegerField


class alternativas(models.Model):
    alternativa= CharField(max_length=100)
    descripcion_breve = CharField(max_length=400, blank=True)
    url_info= URLField(blank=True)

class imagen_patologica(models.Model):
    imagen_con_patologia= ImageField(upload_to='estudio/images/')
    titulo= CharField(max_length=100)
    Informacion_adicional= CharField(max_length=200, default='Dolor estomacal')