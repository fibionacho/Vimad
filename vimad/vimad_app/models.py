from django.db import models
from django_extensions.db.fields import AutoSlugField


class Estudio(models.Model):
    nombre=models.CharField(max_length=50)
    fec_fundacion=models.DateField()

    def __str__(self):
        return self.nombre
    
class Director(models.Model):
    nombre=models.CharField(max_length=50)
    fec_nacimiento=models.DateField()
    nacionalidad=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Actor(models.Model):
    nombre=models.CharField(max_length=50)
    fec_nacimiento=models.DateField()
    nacionalidad=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre   
    
class Corto(models.Model):
    titulo=models.CharField(max_length=50)
    puntuacion=models.CharField(max_length=10)
    genero=models.CharField(max_length=50)
    duracion=models.CharField(max_length=3)
    fec_estreno=models.DateField()
    idioma=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    sinopsis=models.TextField(max_length=50)
    imagen=models.ImageField(upload_to='', null=True)
    video=models.FileField(upload_to='',null=True)

    def __str__(self):
        return self.titulo

class Dirige(models.Model):
    nombre = models.ForeignKey(Director, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Corto, on_delete=models.CASCADE)
    id = MultiFieldPK('nombre', 'titulo')

    def __str__(self):
        return self.id

class Actua(models.Model):
    nombre = models.ForeignKey(Actor, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Corto, on_delete=models.CASCADE)
    id = MultiFieldPK('nombre', 'titulo')

    def __str__(self):
        return self.id