from django.db import models

######################### Classes de Atividades por Restaurante #########################
class BotafogoAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )

    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class IpanemaAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class FMALLAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())    

class RDBAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class RioSulAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())

class TijucaAtividade(models.Model):
    atividade_choice = (
        ('Folga','Folga'),('Produção','Produção'),('Finalização','Finalização'),('Slash','Slash'),('QA','QA'),('Inventário','Inventário'),('Fechamento','Fechamento'),('Almoço','Almoço'),('Janta','Janta')
        )

    hora_choice = (
        ('7hrs','7 Hrs'),('8hrs','8 Hrs'),('9hrs','9 Hrs'),('10hrs','10 Hrs'),('11hrs','11 Hrs'),('12hrs','12 Hrs'),('13hrs','13 Hrs'),('14hrs','14 Hrs'),
        ('15hrs','15 Hrs'),('16hrs','16 Hrs'),('17hrs','17 Hrs'),('18hrs','18 Hrs'),('19hrs','19 Hrs'),('20hrs','20 Hrs'),('21hrs','21 Hrs'),('22hrs','22 Hrs'),
        ('23hrs','23 Hrs'),('00hrs','00 Hrs'),('01hrs','01 Hrs')
        )

    praca_choice = (
        ('Nenhuma','Nenhuma'),('Combinados','Combinados'),('Entradas','Entradas'),('Entradas Sushibar','Entradas Sushibar'),
        ('Rolls','Rolls'),('Rolls Quentes','Rolls Quentes'),('Rolls Frios','Rolls Frios'),('Brisas Duplas Entradas','Brisas Duplas Entradas'),
        ('Fritadeira','Fritadeira'),('Fogão','Fogão'),('Sobremesas','Sobremesas'),('Sushi Brisas','Sushi Brisas'),('Limpeza','Limpeza'),
        ('Produção','Produção')
        )


    hora = models.CharField(max_length=250, choices=hora_choice, null=False, blank=False)
    atividade = models.CharField(max_length=250, choices=atividade_choice, null=False, blank=False)
    praca = models.CharField(max_length=250, choices=praca_choice, default='Nenhuma')

    def __str__(self):
        return str(self.get_atividade_display())    


####################### Classes de Escala por restaurante #########################

class BotafogoEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(BotafogoAtividade)
    
    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])
    

class IpanemaEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(IpanemaAtividade)

    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])

class RDBEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(RDBAtividade)

    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])

class FMALLEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(FMALLAtividade)

    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])

class TijucaEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(TijucaAtividade)

    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])
class RioSulEscala(models.Model):
    dia_choice = (
        ('Domingo','Domingo'),('Segunda','Segunda'),('Terça','Terça'),('Quarta','Quarta'),('Quinta','Quinta'),('Sexta','Sexta'),('Sábado','Sábado')
        )

    funcionario = models.CharField(max_length=100, null=False, blank=False)
    dia = models.CharField(max_length=250, choices=dia_choice, null=False, blank=False)
    atividade = models.ManyToManyField(RioSulAtividade)

    def atividades(self):
        return "\n".join([p.atividade for p in self.atividade.all()])