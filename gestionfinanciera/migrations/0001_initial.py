# Generated by Django 3.0.9 on 2020-08-04 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Type', models.CharField(max_length=250)),
                ('Number', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Bank', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=250)),
                ('Application_Date', models.DateTimeField()),
                ('Date_Of_Receipt', models.DateTimeField()),
                ('Certificate_Days', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Certified_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Payment_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_value', models.CharField(max_length=250)),
                ('Pay_Date', models.DateTimeField()),
                ('Banking_Entity', models.CharField(max_length=250)),
                ('Disbursement_Amount', models.CharField(max_length=250)),
                ('Odds_Number', models.CharField(max_length=250)),
                ('Disbursement_Value', models.CharField(max_length=250)),
                ('Adviser', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Obligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Obligation_Number', models.CharField(max_length=250)),
                ('Type', models.CharField(max_length=250)),
                ('Entity_Obligation', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
                ('Outstanding_Fees', models.IntegerField()),
                ('Quota_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Future_Value_Portfolio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Certified_Value_Obligation', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Saving_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Buyer', models.CharField(max_length=250)),
                ('Default_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Default_Time', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Buy_Mora_Portfolio', models.CharField(max_length=250)),
                ('Reported_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Offer_Value_To_Entity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Negotiated_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Negotiated_With', models.CharField(max_length=250)),
                ('Certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Certificate')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payroll_Company', models.CharField(max_length=250)),
                ('Payroll_Type', models.CharField(max_length=250)),
                ('Salary_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Permanent_Income', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Social_Security', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Law_Applies', models.CharField(max_length=250)),
                ('Permanent_Discounts', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Non_Concellable_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Payment_Capacity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Contract_Type', models.CharField(max_length=250)),
                ('Bonding_Date', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=250)),
                ('Labor_Company', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('Relationship', models.CharField(max_length=250)),
                ('Cell_Phone', models.IntegerField()),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Right_Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Application', models.CharField(max_length=250)),
                ('Send_Date', models.DateTimeField()),
                ('Filed_Number', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Reply_Date', models.DateTimeField()),
                ('Process_state', models.CharField(max_length=250)),
                ('Reply', models.CharField(max_length=600)),
                ('Guardianship_Date', models.DateTimeField()),
                ('Court', models.CharField(max_length=250)),
                ('Guardianship_Response_Date', models.DateTimeField()),
                ('Observation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Management_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Advisor_Records', models.CharField(max_length=250)),
                ('Origin', models.CharField(max_length=250)),
                ('Campaign', models.CharField(max_length=250)),
                ('Customer_Referrer', models.CharField(max_length=250)),
                ('Actual_state', models.CharField(max_length=250)),
                ('Campus', models.CharField(max_length=250)),
                ('Outcome', models.CharField(max_length=250)),
                ('Result_Date', models.DateTimeField()),
                ('Date_Of_Contact', models.DateTimeField()),
                ('Bank_Accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Bank_Accounts')),
                ('Disbursement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Disbursement')),
                ('Financial_Obligation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Financial_Obligation')),
                ('Right_Petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Right_Petition')),
            ],
        ),
        migrations.AddField(
            model_name='financial_obligation',
            name='Payroll_Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Payroll_Client'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Identification', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('Cell_Phone', models.IntegerField()),
                ('Phone', models.IntegerField()),
                ('Date_of_birth', models.DateTimeField()),
                ('Stratum', models.IntegerField()),
                ('Neighborhood', models.CharField(max_length=250)),
                ('Management_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
                ('Payroll_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Payroll_Client')),
                ('Reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Bank_Accounts')),
            ],
        ),
    ]
