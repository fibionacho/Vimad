from django.contrib import admin
from .models import Estudio, Director, Actor, Corto, Dirige, Actua

# Register your models here.
admin.site.register(Estudio)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Corto)
admin.site.register(Dirige)
admin.site.register(Actua)