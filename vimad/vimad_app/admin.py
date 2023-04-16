from django.contrib import admin
from .models import Estudio
from .models import Director
from .models import Actor
from .models import Corto
from .models import Dirige
from .models import Actua

# Register your models here.
admin.site.register(Estudio)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Corto)
admin.site.register(Dirige)
admin.site.register(Actua)