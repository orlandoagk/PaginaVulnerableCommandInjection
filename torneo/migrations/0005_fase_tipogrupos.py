# Generated by Django 2.2.2 on 2019-07-04 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_fase'),
    ]

    operations = [
        migrations.AddField(
            model_name='fase',
            name='tipoGrupos',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='A', max_length=1),
        ),
    ]