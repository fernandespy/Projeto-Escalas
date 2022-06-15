from django.contrib import admin
from Escala.models import EscalaBotafogo, Atividade, Ipanema

@admin.register(EscalaBotafogo)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia']
    list_filter = ['funcionario', 'dia']

@admin.register(Ipanema)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia']
    list_filter = ['funcionario', 'dia']

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

