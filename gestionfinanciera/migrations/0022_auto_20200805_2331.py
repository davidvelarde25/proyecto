# Generated by Django 3.0.8 on 2020-08-06 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0021_auto_20200805_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Cell_Phone',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='City',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='Date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='client',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='Identification',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='Name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='Neighborhood',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Stratum',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Date_Of_Contact',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Result_Date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Guardianship_Date',
            field=models.DateField(default=datetime.date),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Reply_Date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Send_Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]