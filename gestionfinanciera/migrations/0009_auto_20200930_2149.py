# Generated by Django 3.0.9 on 2020-10-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0008_remove_financial_obligation_fk_payroll_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actual_state',
            name='Detail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='advisor_records',
            name='Name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
