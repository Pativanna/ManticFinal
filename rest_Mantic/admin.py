from django.contrib import admin
from .models import Categoria,juego,consola,figura,marca
# Register your models here.
admin.site.register(Categoria)
admin.site.register(juego)
admin.site.register(consola)
admin.site.register(figura)
admin.site.register(marca)

