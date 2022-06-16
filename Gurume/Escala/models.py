from django.db import models

# Classes de Atividades por Restaurante
class BotafogoAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class IpanemaAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class FMALLAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())    

class RDBAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class RioSulAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class TijucaAtividade(models.Model):
    atividade_choice = (
        ('Fol','Folga'),('Pro','Produção'),('Fin','Finalização'),('Sla','Slash'),('QA','QA'),('Inv','Inventário'),('Fec','Fechamento'),('Alm','Almoço'),('Jan','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('N','Nenhuma'),('C','Combinados'),('ENT','Entradas'),('ES','Entradas Sushibar'),
        ('Rol','Rolls'),('RQ','Rolls Quentes'),('RF','Rolls Frios'),('BDE','Brisas Duplas Entradas'),
        ('Fri','Fritadeira'),('FOG','Fogão'),('Sob','Sobremesas'),('Sus','Sushi Brisas'),('Lim','Limpeza'),
        ('Pro','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())    

# Classes de Escala por restaurante
class BotafogoEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(BotafogoAtividade)

class IpanemaEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(IpanemaAtividade)


class RDBEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(RDBAtividade)

class FMALLEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(FMALLAtividade)

class TijucaEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(TijucaAtividade)

class RioSulEscala(models.Model):
    dia_choice = (
        ('Dom','Domingo'),('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(RioSulAtividade)