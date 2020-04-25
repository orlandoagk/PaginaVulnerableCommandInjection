# Generated by Django 2.2.2 on 2019-07-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0007_auto_20190707_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='fechaFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(default='2019-I', editable=False, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='primerPuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primerPuesto', to='torneo.Capitan'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='segundoPuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='segundoPuesto', to='torneo.Capitan'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='tercerPuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tercerPuesto', to='torneo.Capitan'),
        ),
    ]
