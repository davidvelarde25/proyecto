
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actual_State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Advisor_Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Identification', models.CharField(blank=True, max_length=250)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Address', models.CharField(blank=True, max_length=250)),
                ('City', models.CharField(blank=True, max_length=250)),
                ('Cell_Phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('Phone', models.IntegerField(blank=True)),
                ('Date_of_birth', models.DateField(blank=True, default=datetime.datetime.now)),
                ('Stratum', models.IntegerField(blank=True)),
                ('Neighborhood', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Referrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Management_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origin', models.CharField(blank=True, max_length=250, null=True)),
                ('Campaign', models.CharField(blank=True, max_length=250)),
                ('Campus', models.CharField(blank=True, max_length=250, null=True)),
                ('Outcome', models.CharField(blank=True, max_length=250, null=True)),
                ('Result_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Date_Of_Contact', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Status_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Customer_Referrer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.customer_referrer')),
                ('Fk_Actual_State', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.actual_state')),
                ('Fk_Advisor_Records', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.advisor_records')),
                ('Fk_Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.client')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payroll_Company', models.CharField(blank=True, max_length=250)),
                ('Payroll_Type', models.CharField(blank=True, max_length=250)),
                ('Salary_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Permanent_Income', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Social_Security', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Law_Applies', models.CharField(blank=True, max_length=250)),
                ('Permanent_Discounts', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Non_Concellable_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Payment_Capacity', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Bonding_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Fk_Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.client')),
            ],
        ),
        migrations.CreateModel(
            name='Simulation_Banking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank', models.CharField(blank=True, max_length=250)),
                ('Number_Quotas', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Factor', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Estimed_Credit', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Quota_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Fk_Client_Payroll', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.payroll_client')),
            ],
        ),
        migrations.CreateModel(
            name='Right_Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Application', models.CharField(blank=True, max_length=250)),
                ('Line', models.CharField(blank=True, max_length=250)),
                ('Send_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Filed_Number', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Reply_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Process_State', models.CharField(blank=True, max_length=250)),
                ('Reply', models.CharField(blank=True, max_length=600)),
                ('Guardianship_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Court', models.CharField(blank=True, max_length=250)),
                ('Guardianship_Response_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Observation', models.CharField(blank=True, max_length=1000)),
                ('Fk_Management_Type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=250)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Address', models.CharField(blank=True, max_length=250, null=True)),
                ('Labor_Company', models.CharField(blank=True, max_length=250, null=True)),
                ('City', models.CharField(blank=True, max_length=250, null=True)),
                ('Relationship', models.CharField(blank=True, max_length=250, null=True)),
                ('Cell_Phone', models.DecimalField(blank=True, decimal_places=0, max_digits=20)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Fk_Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.client')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Obligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Obligation_Number', models.CharField(blank=True, max_length=250)),
                ('Type', models.CharField(blank=True, max_length=250)),
                ('Entity_Cooperative', models.CharField(blank=True, max_length=250)),
                ('State', models.CharField(blank=True, max_length=250)),
                ('Outstanding_Fees', models.IntegerField(blank=True)),
                ('Quota_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Future_Value_Portfolio', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Certified_Value_Obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Saving_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Buyer', models.CharField(blank=True, max_length=250)),
                ('Default_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Default_Time', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Buy_Mora_Portfolio', models.CharField(blank=True, max_length=250)),
                ('Reported_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Offer_Value_To_Entity', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Negotiated_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Negotiated_With', models.CharField(blank=True, max_length=250)),
                ('Fk_Management_Type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Future_Value_Portfolio', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Payment_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Pay_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Banking_Entity', models.CharField(blank=True, max_length=250)),
                ('Disbursement_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Number_Installment', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Disbursement_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Adviser', models.CharField(blank=True, max_length=250)),
                ('State', models.CharField(blank=True, max_length=250)),
                ('Fk_Management_Type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=250)),
                ('Application_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Date_Of_Receipt', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Certificate_Days', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Certified_Value', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Payment_Date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('Fk_Financial_Obligation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.financial_obligation')),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Type', models.CharField(blank=True, max_length=250)),
                ('Number', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('Bank', models.CharField(blank=True, max_length=250)),
                ('State', models.CharField(blank=True, max_length=250)),
                ('Fk_Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.client')),
            ],
        ),
    ]
