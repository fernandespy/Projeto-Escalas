# Generated by Django 4.0.5 on 2022-06-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escala', '0002_escala_praca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='praca',
            field=models.CharField(choices=[('C', 'Combinados'), ('E', 'Entradas'), ('R', 'Rolls'), ('B', 'Brisas'), ('N', 'Nenhuma')], default='Nenhuma', max_length=250),
        ),
    ]
