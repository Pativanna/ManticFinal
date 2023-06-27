from django import forms
from .models import Categoria, juego, consola, figura, marca
from django.forms import ModelForm

class juegoForm(ModelForm):
    model = juego
    fields = "__all__"