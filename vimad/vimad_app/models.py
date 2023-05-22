from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

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
    puntuacion=models.IntegerField()
    genero=models.CharField(max_length=50)
    duracion=models.CharField(max_length=3)
    fec_estreno=models.DateField()
    idioma=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    sinopsis=models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='cortos/', default='cortos/default.png', blank=True)
    video = models.FileField(upload_to='videos/', default='', blank=True)
    director = models.ManyToManyField(Director, through='Dirige')
    actor = models.ManyToManyField(Actor, through='Actua')
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
            while Corto.objects.filter(slug=self.slug).exists():
                self.slug = "{}-{}".format(slugify(self.titulo), get_random_string(5))
        super(Corto, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Dirige(models.Model):
    corto = models.ForeignKey(Corto, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.director} dirige {self.corto}'

class Actua(models.Model):
    corto = models.ForeignKey(Corto, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.actor} actúa en {self.corto}'