# Generated by Django 3.0.9 on 2020-09-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0003_payroll_client_contract_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management_type',
            name='Outcome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
