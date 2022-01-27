from django.db import models

# Create your models here.
class Lottery(models.Model):
    timestamp = models.CharField(max_length=120, default="")
    status = models.IntegerField
    numero1 = models.CharField(max_length=5, default="")
    numero2 = models.CharField(max_length=5, default="")
    numero3 = models.CharField(max_length=5, default="")
    numero4 = models.CharField(max_length=5, default="")
    numero5 = models.CharField(max_length=5, default="")
    numero6 = models.CharField(max_length=5, default="")
    numero7 = models.CharField(max_length=5, default="")
    numero8 = models.CharField(max_length=5, default="")
    numero9 = models.CharField(max_length=5, default="")
    numero10 = models.CharField(max_length=5, default="")
    numero11 = models.CharField(max_length=5, default="")
    numero12 = models.CharField(max_length=5, default="")
    numero13 = models.CharField(max_length=5, default="")
    numero14 = models.CharField(max_length=5, default="")
    numero15 = models.CharField(max_length=5, default="")
    numero16 = models.CharField(max_length=5, default="")
    numero17 = models.CharField(max_length=5, default="")
    numero18 = models.CharField(max_length=5, default="")
    numero19 = models.CharField(max_length=5, default="")
    numero20 = models.CharField(max_length=5, default="")
    fraseSorteoPDF = models.TextField
    fraseListaPDF = models.TextField
    listaPDF = models.TextField
    urlAudio = models.TextField
    error = models.IntegerField

    def _str_(self):
        return self.timestamp

class ArgLottery(models.Model):
    tipo_quiniela = models.TextField(max_length = 50, default="" )
    nombre_sorteo = models.TextField(max_length = 20, default="" )
    fecha =  models.TextField(max_length = 50, default="" )
    timezone_type = models.IntegerField(default=-3)
    timezone = models.TextField(max_length=20, blank=True )
    letras = models.TextField(max_length=20, blank=True, null=True  )
    premios = models.TextField(max_length=20,  blank=True, null=True )
    pozo_proximo = models.TextField(max_length=20, blank=True, null=True )
    
    numero1 = models.CharField(max_length=5, default="")
    numero2 = models.CharField(max_length=5, default="")
    numero3 = models.CharField(max_length=5, default="")
    numero4 = models.CharField(max_length=5, default="")
    numero5 = models.CharField(max_length=5, default="")
    numero6 = models.CharField(max_length=5, default="")
    numero7 = models.CharField(max_length=5, default="")
    numero8 = models.CharField(max_length=5, default="")
    numero9 = models.CharField(max_length=5, default="")
    numero10 = models.CharField(max_length=5, default="")
    numero11 = models.CharField(max_length=5, default="")
    numero12 = models.CharField(max_length=5, default="")
    numero13 = models.CharField(max_length=5, default="")
    numero14 = models.CharField(max_length=5, default="")
    numero15 = models.CharField(max_length=5, default="")
    numero16 = models.CharField(max_length=5, default="")
    numero17 = models.CharField(max_length=5, default="")
    numero18 = models.CharField(max_length=5, default="")
    numero19 = models.CharField(max_length=5, default="")
    numero20 = models.CharField(max_length=5, default="")
    
    def _str_(self):
        return self.nombre_sorteo
