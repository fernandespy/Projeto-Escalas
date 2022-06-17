from django.contrib import admin
from Escala.models import BotafogoEscala, IpanemaEscala, FMALLEscala, RDBEscala, RioSulEscala, TijucaEscala

@admin.register(BotafogoEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']
    

@admin.register(IpanemaEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']

@admin.register(FMALLEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia','hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']    

@admin.register(RDBEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']

@admin.register(RioSulEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']

@admin.register(TijucaEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'hora', 'funcao', 'praca']
    list_filter = ['funcionario', 'dia']
