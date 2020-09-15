from django.db import models
import datetime


# Create your models here.

#creamos la tabla cliente donde se guadan todos los datos que se le solicitan al cliente
class Client(models.Model):
    Name = models.CharField(max_length=250, null=False)
    Identification = models.CharField(max_length=250, null=False,blank=True)
    Email = models.EmailField(max_length =254, null= False, blank=True)
    Address = models.CharField(max_length=250, null=False,blank=True)
    City = models.CharField(max_length=250, null=False, blank=True)
    Cell_Phone = models.DecimalField(max_digits=20, decimal_places=0, null=False)
    Phone = models.IntegerField(null=True, blank=True)
    Date_of_birth = models.DateField(default=datetime.datetime.now, blank=True,null=True)
    Stratum = models.IntegerField(null=True, blank=True)
    Neighborhood = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.Name)

# modelos de las Advisor_Records
class Advisor_Records(models.Model):
    Name = models.CharField(max_length=120, blank=True)
    #activo = models.BooleanField(default="true")

    def __str__(self):
        return '{}'.format(self.Name)

# modelos de las Customer_Referrer
class Customer_Referrer(models.Model):
    Name = models.CharField(max_length=120, blank=True, null=True)
    #activo = models.BooleanField(default="true")

    def __str__(self):
        return '{}'.format(self.Name)

# modelos de las Customer_Referrer
class Actual_State(models.Model):
    Detail = models.CharField(max_length=120,blank=True)
    def __str__(self):
        return '{}'.format(self.Detail)

# TABLA TIPO DE GESTION ENLA EMPPRESA
class Management_Type(models.Model):
    Origin = models.CharField(max_length=250, null=True,blank=True)
    Campaign = models.CharField(max_length=250, null=False,blank=True)
    Fk_Customer_Referrer = models.ForeignKey(Customer_Referrer, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo
    Campus = models.CharField(max_length=250, null=True,blank=True)
    Outcome = models.CharField(max_length=250, null=True,blank=True)
    Result_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Date_Of_Contact = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Status_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Fk_Client  = models.ForeignKey(Client, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo
    Fk_Advisor_Records  = models.ForeignKey(Advisor_Records, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo
    Fk_Actual_State = models.ForeignKey(Actual_State, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo

#  modelo  de los datos de las referencias de los usuarios
class Reference(models.Model):
    Name = models.CharField(max_length=250, null=False,blank=True)
    Email = models.EmailField(max_length =254, null= True,blank=True)
    Address = models.CharField(max_length=250, null=True,blank=True)
    Labor_Company = models.CharField(max_length=250, null=True,blank=True)
    City = models.CharField(max_length=250, null=True,blank=True)
    Relationship = models.CharField(max_length=250, null=True,blank=True)
    Cell_Phone = models.DecimalField(max_digits=20, decimal_places=0, null=False,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Fk_Client = models.ForeignKey(Client, null=True, on_delete = models.CASCADE,blank=True)
    def __str__(self):
        return '{}'.format(self.Name)

# tabla nomina cliente
class Payroll_Client(models.Model):

    Payroll_Company = models.CharField(max_length=250, null=False,blank=True)
    Payroll_Type = models.CharField(max_length=250, null=False,blank=True)
    Salary_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True , null=True)
    Permanent_Income = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Social_Security  = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Law_Applies = models.CharField(max_length=250, null=False,blank=True)
    Permanent_Discounts = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Non_Concellable_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Payment_Capacity = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Bonding_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Fk_Client = models.ForeignKey(Client, null=True, on_delete = models.CASCADE,blank=True)
    def __str__(self):
        return '{}'.format(self.Payroll_Company)

# tabla simulacion bancaria
class Simulation_Banking(models.Model):
    Bank = models.CharField(max_length=250, null=False,blank=True)
    Number_Quotas = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Factor = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Estimed_Credit = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Quota_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Fk_Client_Payroll = models.ForeignKey(Payroll_Client, null=True, on_delete = models.CASCADE,blank=True)

# tabla derecho peticion
class Right_Petition(models.Model):
    Type_Application = models.CharField(max_length=250, null=False,blank=True)
    Line = models.CharField(max_length=250, null=False,blank=True)
    Send_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Filed_Number = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    Reply_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Process_State = models.CharField(max_length=250, null=False,blank=True)
    Reply = models.CharField(max_length=600, null=False,blank=True)
    Guardianship_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Court = models.CharField(max_length=250, null=False,blank=True)
    Guardianship_Response_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Observation = models.CharField(max_length=1000, null=False,blank=True)
    Fk_Management_Type = models.ForeignKey(Management_Type, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo

# tabla cuentas bancarias
class Bank_Accounts(models.Model):
    Account_Type = models.CharField(max_length=250, null=False,blank=True)
    Number = models.DecimalField(max_digits=15, decimal_places=0,blank=True, null=True)
    Bank = models.CharField(max_length=250, null=False,blank=True)
    State = models.CharField(max_length=250, null=False,blank=True)
    Fk_Client = models.ForeignKey(Client, null=True, on_delete = models.CASCADE,blank=True)

#creacion tabla desembolso
class Disbursement(models.Model):
    Future_Value_Portfolio = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Payment_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Pay_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Banking_Entity = models.CharField(max_length=250, null=False,blank=True)
    Disbursement_Amount = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Number_Installment = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Disbursement_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Adviser = models.CharField(max_length=250, null=False,blank=True)
    State = models.CharField(max_length=250, blank=True, null=True)
    Fk_Management_Type = models.ForeignKey(Management_Type, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo

# creacion tabla obigaciones  financieras
class Financial_Obligation(models.Model):
    Obligation_Number = models.CharField(max_length=250, null=False,blank=True)
    Type = models.CharField(max_length=250, null=False,blank=True)
    Entity_Cooperative = models.CharField(max_length=250, null=False,blank=True)
    State = models.CharField(max_length=250, null=False,blank=True)
    Outstanding_Fees = models.IntegerField(null=False,blank=True)
    Quota_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Future_Value_Portfolio = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Certified_Value_Obligation = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Saving_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Buyer = models.CharField(max_length=250,blank=True, null=False)
    Default_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Default_Time = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Buy_Mora_Portfolio = models.CharField(max_length=250,blank=True, null=True)
    Reported_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Offer_Value_To_Entity = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Negotiated_Value = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Negotiated_With = models.CharField(max_length=250, null=False,blank=True)
    Fk_Management_Type = models.ForeignKey(Management_Type, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo

# tabla certificados
class Certificate(models.Model):
    Type = models.CharField(max_length=250, null=False,blank=True)
    Application_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Date_Of_Receipt = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Certificate_Days = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Certified_Value =  models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    Payment_Date = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    Fk_Financial_Obligation = models.ForeignKey(Financial_Obligation, null=True, on_delete = models.CASCADE,blank=True) # se crea una llave foranea llamando al modelo categoria
