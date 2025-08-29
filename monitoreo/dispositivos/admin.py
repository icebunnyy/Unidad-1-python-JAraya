from django.contrib import admin

from .models import Categoria, Zona, Dispositivo

admin.site.register([Categoria, zona])


admin.site.register(Dispositivo)