from django.db import models


class Museo(models.Model):
    nombre = models.CharField(max_length=150, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=255)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")
