from django.db import models
import datetime


# Create your models here.

#creamos la tabla cliente donde se guadan todos los datos que se le solicitan al cliente
class Client(models.Model):
    Name = models.CharField(max_length=250, null=False)
    Identification = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    Email = models.EmailField(max_length =254, null= False, blank=True)
    Address = models.CharField(max_length=250, null=False)
    City = models.CharField(max_length=250, null=False, blank=True)
    Cell_Phone = models.DecimalField(max_digits=20, decimal_places=0, null=False)
    Phone = models.IntegerField(null=True, blank=True)
    Date_of_birth = models.DateField(default=datetime.date.today, blank=True)
    Stratum = models.IntegerField(null=True, blank=True)
    Neighborhood = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.Name)

# modelos de las Advisor_Records
class Advisor_Records(models.Model):
    Name = models.CharField(max_length=120)
    #activo = models.BooleanField(default="true")

    def __str__(self):
        return '{}'.format(self.Name)

# modelos de las Customer_Referrer
class Customer_Referrer(models.Model):
    Description = models.CharField(max_length=120)
    #activo = models.BooleanField(default="true")

    def __str__(self):
        return '{}'.format(self.Descripcion)

# modelos de las Customer_Referrer
class Actual_state(models.Model):
    Description = models.CharField(max_length=120)
    #activo = models.BooleanField(default="true")

    def __str__(self):
        return '{}'.format(self.Descripcion)

# TABLA TIPO DE GESTION ENLA EMPPRESA
class Management_type(models.Model):

    Origin = models.CharField(max_length=250, null=True)
    Campaign = models.CharField(max_length=250, null=False)
    Customer_Referrer = models.ForeignKey(Customer_Referrer, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

    Campus = models.CharField(max_length=250, null=True)
    Outcome = models.CharField(max_length=250, null=True)
    Result_Date = models.DateField(default=datetime.date.today, blank=True)
    Date_Of_Contact = models.DateField(default=datetime.date.today, blank=True)
    Client  = models.ForeignKey(Client, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo
    Advisor_Records  = models.ForeignKey(Advisor_Records, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo
    Actual_state = models.ForeignKey(Actual_state, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

# modelo de las bitacoras
class Tracing(models.Model):
    Description = models.CharField(max_length=2000)
    Follow_Date = models.DateField(default=datetime.date.today, blank=True)
    Adviser = models.DateField(default=datetime.date.today, blank=True)
    Management_type  = models.ForeignKey(Management_type, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

#  modelo  de los datos de las referencias de los usuarios
class Reference(models.Model):
    Name = models.CharField(max_length=250, null=False)
    Email = models.EmailField(max_length =254, null= True)
    Address = models.CharField(max_length=250, null=True)
    Labor_Company = models.CharField(max_length=250, null=True)
    City = models.CharField(max_length=250, null=True)
    Relationship = models.CharField(max_length=250, null=True)
    Cell_Phone = models.DecimalField(max_digits=20, decimal_places=0, null=False)
    Phone = models.IntegerField(null=True)
    Client = models.ForeignKey(Client, null=True, on_delete = models.CASCADE)

# tabla nomina cliente
class Payroll_Client(models.Model):
    Payroll_Company = models.CharField(max_length=250, null=False)
    Payroll_Type = models.CharField(max_length=250, null=False)
    Salary_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Permanent_Income = models.DecimalField(max_digits=15, decimal_places=2)
    Social_Security  = models.DecimalField(max_digits=15, decimal_places=2)
    Law_Applies = models.CharField(max_length=250, null=False)
    Permanent_Discounts = models.DecimalField(max_digits=15, decimal_places=2)
    Non_Concellable_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Payment_Capacity = models.DecimalField(max_digits=15, decimal_places=2)
    Contract_Type = models.CharField(max_length=250, null=False)
    Bonding_Date = models.CharField(max_length=250, null=False)
    Client = models.ForeignKey(Client, null=True, on_delete = models.CASCADE)



# tabla derecho peticion
class Right_Petition(models.Model):

    Type_Application = models.CharField(max_length=250, null=False)
    Send_Date = models.DateField(default=datetime.date.today, blank=True)
    Filed_Number = models.DecimalField(max_digits=15, decimal_places=2)
    Reply_Date = models.DateField(default=datetime.date.today, blank=True)
    Process_state = models.CharField(max_length=250, null=True)
    Reply = models.CharField(max_length=600, null=True)
    Guardianship_Date = models.DateField(default=datetime.date.today, blank=True)
    Court = models.CharField(max_length=250, null=True)
    Guardianship_Response_Date = models.DateField(default=datetime.date.today, blank=True)
    Observation = models.CharField(max_length=1000, null=True)
    Management_type = models.ForeignKey(Management_type, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

# tabla cuentas bancarias
class Bank_Accounts(models.Model):
    Account_Type = models.CharField(max_length=250, null=True)
    Number = models.DecimalField(max_digits=15, decimal_places=2)
    Bank = models.CharField(max_length=250, null=True)
    State = models.CharField(max_length=250, null=True)
    Management_type = models.ForeignKey(Management_type, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

#creacion tabla desembolso
class Disbursement(models.Model):
    Payment_value = models.CharField(max_length=250, null=True)
    Pay_Date = models.DateField(default=datetime.date.today, blank=True)
    Banking_Entity = models.CharField(max_length=250, null=True)
    Disbursement_Amount = models.CharField(max_length=250, null=True)
    Odds_Number = models.CharField(max_length=250, null=True)
    Disbursement_Value = models.CharField(max_length=250, null=True)
    Adviser = models.CharField(max_length=250, null=True)
    State = models.CharField(max_length=250, null=True)
    Management_type = models.ForeignKey(Management_type, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

# creacion tabla obigaciones  financieras
class Financial_Obligation(models.Model):
    Obligation_Number = models.CharField(max_length=250, null=False)
    Type = models.CharField(max_length=250, null=False)
    Entity_Obligation = models.CharField(max_length=250, null=False)
    State = models.CharField(max_length=250, null=False)
    Outstanding_Fees = models.IntegerField(null=True)
    Quota_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Future_Value_Portfolio = models.DecimalField(max_digits=15, decimal_places=2)
    Certified_Value_Obligation = models.DecimalField(max_digits=15, decimal_places=2)
    Saving_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Buyer = models.CharField(max_length=250, null=True)
    Default_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Default_Time = models.DecimalField(max_digits=15, decimal_places=2)
    Buy_Mora_Portfolio = models.CharField(max_length=250, null=True)
    Reported_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Offer_Value_To_Entity = models.DecimalField(max_digits=15, decimal_places=2)
    Negotiated_Value = models.DecimalField(max_digits=15, decimal_places=2)
    Negotiated_With = models.CharField(max_length=250, null=True)
    Client =  models.ForeignKey(Client, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo
    Management_type = models.ForeignKey(Management_type, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo

# tabla certificados
class Certificate(models.Model):
    Type = models.CharField(max_length=250, null=False)
    Application_Date = models.DateField(default=datetime.date.today, blank=True)
    Date_Of_Receipt = models.DateField(default=datetime.date.today, blank=True)
    Certificate_Days = models.DecimalField(max_digits=15, decimal_places=2)
    Certified_Value =  models.DecimalField(max_digits=15, decimal_places=2)
    Payment_Date = models.DateField(default=datetime.date.today, blank=True)
    Financial_Obligation = models.ForeignKey(Financial_Obligation, null=True, on_delete = models.CASCADE) # se crea una llave foranea llamando al modelo categoria
