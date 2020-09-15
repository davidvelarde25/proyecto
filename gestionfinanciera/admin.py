from django.contrib import admin

from .models import Reference,Disbursement,Management_Type, Payroll_Client, Certificate, Right_Petition, Bank_Accounts, Disbursement, Financial_Obligation,Client,Advisor_Records, Actual_State,Customer_Referrer

# Register your models here.
admin.site.register(Client)
admin.site.register(Reference)
admin.site.register(Payroll_Client)
admin.site.register(Certificate)
admin.site.register(Right_Petition)
admin.site.register(Bank_Accounts)
admin.site.register(Disbursement)
admin.site.register(Management_Type)
admin.site.register(Financial_Obligation)
admin.site.register(Advisor_Records)
admin.site.register(Customer_Referrer)
admin.site.register(Actual_State)
