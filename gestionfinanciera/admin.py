from django.contrib import admin

from .models import Reference, Payroll_Client, Certificate, Right_Petition, Bank_Accounts, Disbursement, Financial_Obligation, Management_type, Client,Advisor_Records, Actual_state

# Register your models here.
admin.site.register(Client)
admin.site.register(Reference)
admin.site.register(Payroll_Client)
admin.site.register(Certificate)
admin.site.register(Right_Petition)
admin.site.register(Bank_Accounts)
admin.site.register(Disbursement)
admin.site.register(Management_type)
admin.site.register(Financial_Obligation)
admin.site.register(Advisor_Records)
#admin.site.register(Customer_Referrer)
admin.site.register(Actual_state)
