from django.db import models

# Create your models here.

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrecategoria
    
class juego(models.Model):
    idjuego = models.AutoField(primary_key=True)
    nomjuego = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='juegopictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    precio = models.IntegerField()
    nventas = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nomjuego
    

class consola(models.Model):
    idConsola = models.AutoField(primary_key=True)
    nomConsola = models. CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    marca = models.ForeignKey("marca", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='consolapictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    precio = models.IntegerField()
    nventas = models.IntegerField()

    def __str__(self):
        return self.nomConsola
    

class figura(models.Model):
    idFigura = models.AutoField(primary_key=True)
    nomFigura = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='figurapictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    precio = models.IntegerField()
    nventas = models.IntegerField()

    def __str__(self):
        return self.nomFigura
    



class marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nomMarca = models.CharField(max_length=50)

    def __str__(self):
        return self.nomMarca
