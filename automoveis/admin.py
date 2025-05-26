from django.contrib import admin
from automoveis.models import Carro, Moto, Caminhao
# Register your models here.

class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'ano_fabricacao', 'preco', 'tipo_combustivel', 'quilometragem')
    list_display_links = ('id', 'marca', 'modelo')
    search_fields = ('marca','modelo')
    list_per_page = 10
    ordering = ('ano_fabricacao',)
admin.site.register(Carro, CarroAdmin)

class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'ano_fabricacao', 'preco', 'tipo_combustivel', 'cilindrada')
    list_display_links = ('id', 'marca', 'modelo')
    search_fields = ('marca','modelo')
    list_per_page = 10
    ordering = ('ano_fabricacao',)
admin.site.register(Moto, MotoAdmin)

class CaminhaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'ano_fabricacao', 'preco', 'tipo_eixo')
    list_display_links = ('id', 'marca', 'modelo')
    search_fields = ('marca','modelo')
    list_per_page = 10
    ordering = ('ano_fabricacao',)
admin.site.register(Caminhao, CaminhaoAdmin)
