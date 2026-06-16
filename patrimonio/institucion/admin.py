from django.contrib import admin

from .models import Exhibicion, GuiaMuseo, Museo


class GuiaMuseoInline(admin.TabularInline):
    model = GuiaMuseo
    extra = 1


class ExhibicionInline(admin.TabularInline):
    model = Exhibicion
    extra = 1


class MuseoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "ciudad",
        "anio_fundacion",
        "costo_total_produccion",
        "guia_mas_experiencia",
    )
    inlines = [GuiaMuseoInline]


class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "anios_experiencia_guia", "museo")
    inlines = [ExhibicionInline]


admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo, GuiaMuseoAdmin)
admin.site.register(Exhibicion)
