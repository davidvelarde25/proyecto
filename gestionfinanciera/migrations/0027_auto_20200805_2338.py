# Generated by Django 3.0.8 on 2020-08-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0026_auto_20200805_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Stratum',
            field=models.IntegerField(null=True),
        ),
    ]
