# Generated by Django 3.0.9 on 2020-10-01 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0007_financial_obligation_fk_payroll_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial_obligation',
            name='Fk_Payroll_Client',
        ),
    ]
