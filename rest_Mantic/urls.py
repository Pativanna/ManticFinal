from django.urls import path
from .views import index, lista_juego, detalle_juego, detalle_consola, detalle_figura, login

urlpatterns=[
    path('',index, name="index"),
    path('lista_juego',lista_juego,name="lista_juego"),
    path('detalle_juego/<id>',detalle_juego,name="detalle_juego"),
    path('detalle_consola/<id>',detalle_consola,name="detalle_consola"),
    path('detalle_figura/<id>',detalle_figura,name="detalle_figura"),
    path('login',login,name="login"),
]
