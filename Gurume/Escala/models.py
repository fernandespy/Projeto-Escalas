from django.db import models
from multiselectfield import MultiSelectField

class BotafogoEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice, max_choices=4)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())


class IpanemaEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())


class RDBEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())

class FMALLEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())

class TijucaEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())
class RioSulEscala(models.Model):
    funcao_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7','7 Hrs'),('8','8 Hrs'),('9','9 Hrs'),('10','10 Hrs'),('11','11 Hrs'),('12','12 Hrs'),('13','13 Hrs'),('14','14 Hrs'),
        ('15','15 Hrs'),('16','16 Hrs'),('17','17 Hrs'),('18','18 Hrs'),('19','19 Hrs'),('20','20 Hrs'),('21','21 Hrs'),('22','22 Hrs'),
        ('23','23 Hrs'),('00','00 Hrs'),('01','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    hora = MultiSelectField(choices=hora_choice)
    funcao = models.CharField(max_length=250, choices=funcao_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_funcao_display())