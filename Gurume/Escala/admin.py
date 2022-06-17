from django.contrib import admin
from Escala.models import BotafogoAtividade, IpanemaAtividade, FMALLAtividade, RDBAtividade, RioSulAtividade, TijucaAtividade, BotafogoEscala, IpanemaEscala, FMALLEscala, RDBEscala, RioSulEscala, TijucaEscala

@admin.register(BotafogoEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'atividades']
    list_filter = ['funcionario', 'dia']
    

@admin.register(IpanemaEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'atividades']
    list_filter = ['funcionario', 'dia']

@admin.register(FMALLEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia','atividades']
    list_filter = ['funcionario', 'dia']    

@admin.register(RDBEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'atividades']
    list_filter = ['funcionario', 'dia']

@admin.register(RioSulEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'atividades']
    list_filter = ['funcionario', 'dia']

@admin.register(TijucaEscala)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['funcionario', 'dia', 'atividades']
    list_filter = ['funcionario', 'dia']

################ Atividades #################

@admin.register(BotafogoAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

@admin.register(IpanemaAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

@admin.register(FMALLAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

@admin.register(RDBAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

@admin.register(RioSulAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']

@admin.register(TijucaAtividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['hora', 'atividade', 'praca']
    list_filter = ['hora', 'atividade']
