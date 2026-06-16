from django.db import models
from django.db.models import Sum


class Museo(models.Model):
    nombre = models.CharField(max_length=150, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre

    def costo_total_produccion(self):
        total = Exhibicion.objects.filter(guia_asistente__museo=self).aggregate(
            Sum("costo_produccion")
        )["costo_produccion__sum"]
        return total or 0.00

    def guia_mas_experiencia(self):
        guias = self.guias.all()
        if not guias.exists():
            return "Sin guías asignados"

        max_experiencia = max(guia.anios_experiencia_guia for guia in guias)
        mejores_guias = guias.filter(anios_experiencia_guia=max_experiencia)

        return ", ".join([g.nombre_completo for g in mejores_guias])


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=255)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return f"{self.nombre_completo} ({self.museo.nombre})"


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=150)

    guia_asistente = models.ForeignKey(
        GuiaMuseo, on_delete=models.CASCADE, related_name="exhibiciones"
    )

    def __str__(self):
        return self.titulo_exhibicion
