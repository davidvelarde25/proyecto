from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import (Client, Reference,Simulation_Banking, Customer_Referrer,
 Management_Type,Advisor_Records, Certificate,Payroll_Client, Reference,
 Financial_Obligation, Right_Petition, Bank_Accounts,Disbursement,Actual_State)
from django.contrib.auth.models import User
from django.urls import reverse
# vistas basadas en clase
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import DetailView

# importamos el logging
import logging

#importamos el formulario
'''from .forms import ClienteForm

def Client(request):
    template_name = 'client_form.html'
    form = ClienteForm()
    if request.method == ' POST':
        form= ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request, template_name, {'form':form})

'''

# muestra todos los clientes
def index(request):
    dataClient = Client.objects.all()
    return render(request, "base.html", { "clientes" : dataClient })

# clase para listar los clientes
class ClientView(ListView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_list.html'
    context_object_name = 'clientes'

# clase para crear los clientes
class ClientCreate(CreateView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_form.html'
    fields = ['Name', 'Identification', 'Email','Address','City','Cell_Phone',
    'Phone', 'Date_of_birth','Stratum','Neighborhood']

    def get_success_url(self):
        return reverse('listarcliente')

# clase para actualziar los clientes
class ClientUpdate(UpdateView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_edit.html'
    fields = ['Name', 'Identification', 'Email','Address','City','Cell_Phone',
    'Phone', 'Date_of_birth','Stratum','Neighborhood']

    def get_success_url(self):
        return reverse('listarcliente')

# clase para crear el tipo de gestion de un usuario
class ManagementTypeCreate(CreateView):
    model = Management_Type
    template_name = 'gestionfinanciera/management_type_form.html'
    fields = ['Origin', 'Campaign', 'Fk_Customer_Referrer','Campus','Outcome',
    'Result_Date','Date_Of_Contact', 'Status_Date','Fk_Client',
    'Fk_Advisor_Records','Fk_Actual_State']

     #se sobreescribe este método para obtener información de otros modelos
    def get_context_data(self,**kwargs):
        context = super(ManagementTypeCreate,self).get_context_data(**kwargs)
        context['customer_referrer'] = Customer_Referrer.objects.all()
        context['advisor_records'] = Advisor_Records.objects.all()
        context['actual_state'] = Actual_State.objects.all()
        context['clientId'] = self.kwargs['pk']
        #context['client'] = Client.objects.all()
        return context
    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar la gestion que se le va a realziar al cliente
class ManagementTypeView(ListView):
    model = Management_Type
    template_name = 'gestionfinanciera/management_type_list.html'
    #context_object_name = 'tipogestion'

    def get_context_data(self,**kwargs):
        context = super(ManagementTypeView,self).get_context_data(**kwargs)
        context['tipogestion'] = Management_Type.objects.filter(Fk_Client=self.kwargs['pk'])
        context['clientId'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('editarcliente')

# clase para actualizar el tipo de gestion de un usuario
class ManagementTypeUpdate(UpdateView):
    model = Management_Type
    template_name = 'gestionfinanciera/management_type_update.html'
    fields=['Origin', 'Campaign', 'Fk_Customer_Referrer','Campus','Outcome',
    'Result_Date','Date_Of_Contact', 'Status_Date','Fk_Client',
    'Fk_Advisor_Records','Fk_Actual_State']

     #se sobreescribe este método para obtener información de otros modelos

    def get_context_data(self,**kwargs):
        context = super(ManagementTypeUpdate,self).get_context_data(**kwargs)
        context['tipogestion'] = Management_Type.objects.filter(Fk_Client=self.kwargs['pk'])
        context['actual_state'] = Actual_State.objects.all()
        context['customer_referrer'] = Customer_Referrer.objects.all()
        context['advisor_records'] = Advisor_Records.objects.all()
        context['client'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('editarcliente')

# clase para crear el la nomina del cliente
class PayrollClientCreate(CreateView):
    model = Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_form.html'
    fields=['Payroll_Company', 'Payroll_Type', 'Contract_Type', 'Salary_Value',
    'Permanent_Income','Social_Security','Law_Applies','Permanent_Discounts',
    'Non_Concellable_Value','Payment_Capacity','Bonding_Date','Fk_Client']

    def get_context_data(self,**kwargs):
        context = super(PayrollClientCreate,self).get_context_data(**kwargs)
        context['client'] = Client.objects.all()
        context['clientId'] = self.kwargs['pk']

        return context

    def get_success_url(self):

        return reverse('listarnomina', args=('1'))

# clase para listar las nominas de los clientes
class PayrollClientView(ListView):
    model = Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_list.html'
    #context_object_name = 'nomina'
    def get_context_data(self,**kwargs):
        context = super(PayrollClientView,self).get_context_data(**kwargs)
        context['nomina'] = Payroll_Client.objects.filter(Fk_Client=self.kwargs['pk'])
        context['clientId'] = self.kwargs['pk']
        return context

# clase para actualziar las referencias de los clientes
class PayrollClientUpdate(UpdateView):
    model = Payroll_Client
    #context_object_name = 'nomina'
    template_name = 'gestionfinanciera/Client/payroll_client_edit.html'
    fields=['Payroll_Company', 'Payroll_Type','Contract_Type', 'Salary_Value',
    'Permanent_Income','Social_Security','Law_Applies','Permanent_Discounts',
    'Non_Concellable_Value','Payment_Capacity','Bonding_Date','Fk_Client']

    def get_context_data(self,**kwargs):
        context = super(PayrollClientUpdate,self).get_context_data(**kwargs)
        context['nomina'] = Payroll_Client.objects.filter(Fk_Client=self.kwargs['pk'])
        context['client'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('listarnomina')

# se crea la clase para eliminar las nominas
class PayrollClientDelete(DeleteView):
    model= Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_delete.html'
    def get_success_url(self):
        return reverse('listarnomina',args=('1') )

# clase para crear las referencias del cliente
class ReferenceCreate(CreateView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_form.html'
    fields = ['Name','Email','Address','Labor_Company','City','Relationship',
    'Cell_Phone','Phone','Fk_Client']

    def get_context_data(self,**kwargs):
        context = super(ReferenceCreate,self).get_context_data(**kwargs)
        context['client'] = Client.objects.all()
        context['clientId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar las referencias de los clientes
class ReferenceView(ListView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_list.html'

    def get_context_data(self,**kwargs):
        context = super(ReferenceView,self).get_context_data(**kwargs)
        #context['nomina'] = model.objects.filter(Fk_Client=self.kwargs['pk'])
        context['referencia'] = Reference.objects.all()
        context['clientId'] = self.kwargs['pk']
        return context

# clase para actualziar las referencias de los clientes
class ReferenceUpdate(UpdateView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_edit.html'
    fields = ['Name', 'Email','Address','Labor_Company','Cell_Phone',
    'Phone', 'City','Relationship','Fk_Client']

    def get_success_url(self):
        return reverse('editarcliente' )

# se crea la clase para eliminar las referencias
class ReferenceDelete(DeleteView):
    model= Reference
    def get_success_url(self):
        return reverse('listarreferencia')

# clase para crear las obligaciones de los clientes
class FinancialObligationCreate(CreateView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_form.html'
    fields = ['Obligation_Number', 'Type', 'Entity_Cooperative',
    'State','Outstanding_Fees','Quota_Value','Future_Value_Portfolio',
    'Certified_Value_Obligation','Saving_Value','Buyer','Default_Value',
    'Default_Time','Buy_Mora_Portfolio','Reported_Value','Offer_Value_To_Entity',
    'Negotiated_Value','Negotiated_With','Fk_Management_Type']

    def get_context_data(self,**kwargs):
        context = super(FinancialObligationCreate,self).get_context_data(**kwargs)
        context['obligacion'] = Financial_Obligation.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_type'] = Management_Type.objects.all()
        context['management_typeId'] = self.kwargs['pk']
        context['clientId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar las referencias de los clientes
class FinancialObligationView(ListView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_list.html'


    def get_context_data(self,**kwargs):
        context = super(FinancialObligationView,self).get_context_data(**kwargs)
        context['obligacion'] = Financial_Obligation.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

# clase para actualziar las referencias de los clientes
class FinancialObligationUpdate(UpdateView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_edit.html'
    fields = ['Obligation_Number', 'Type', 'Entity_Cooperative',
    'State','Outstanding_Fees','Quota_Value','Future_Value_Portfolio',
    'Certified_Value_Obligation','Saving_Value','Buyer','Default_Value',
    'Default_Time','Buy_Mora_Portfolio','Reported_Value','Offer_Value_To_Entity',
    'Negotiated_Value','Negotiated_With','Fk_Management_Type']

    def get_context_data(self,**kwargs):
        context = super(FinancialObligationUpdate,self).get_context_data(**kwargs)
        context['Financial_Obligation'] = Financial_Obligation.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# se crea la clase para eliminar las referencias

class FinancialObligationDelete(DeleteView):
    model= Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_delete.html'
    def get_success_url(self):
        return reverse('listarobligacion',args=('2') )

# cl3ase para crear el certificado
class CertificateCreate(CreateView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_form.html'
    fields = ['Type','Application_Date', 'Date_Of_Receipt','Certificate_Days',
    'Certified_Value','Payment_Date','Fk_Financial_Obligation']

    def get_context_data(self,**kwargs):
        context = super(CertificateCreate,self).get_context_data(**kwargs)
        context['Financial_Obligation'] = Financial_Obligation.objects.all()
        context['obligacionId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('listarcertificado')

# clase para listar los certifiados de los clientes
class CertificateView(ListView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_list.html'
    context_object_name = 'certificado'

    def get_context_data(self,**kwargs):
        context = super(CertificateView,self).get_context_data(**kwargs)
        context['certificado'] = Certificate.objects.filter(Fk_Financial_Obligation=self.kwargs['pk'])
        context['certificateId'] = self.kwargs['pk']
        return context

# clase para actualziar los certificados de los clientes
class CertificateUpdate(UpdateView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_edit.html'
    fields = ['Type','Application_Date', 'Date_Of_Receipt','Certificate_Days',
    'Certified_Value','Payment_Date','Fk_Financial_Obligation']

    def get_context_data(self,**kwargs):
        context = super(CertificateUpdate,self).get_context_data(**kwargs)
        context['certificado'] = Certificate.objects.filter(Fk_Financial_Obligation=self.kwargs['pk'])
        context['obligacionId'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('editarcliente')

# se crea la clase para eliminar las certificados
class CertificateDelete(DeleteView):
    model= Certificate
    def get_success_url(self):
        return reverse('eliminarcertificado')

# clase para crear los derechos de peticion
class RightPetitionCreate(CreateView):
    model = Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_form.html'
    fields = ['Type_Application','Line','Send_Date','Filed_Number','Reply_Date',
    'Process_State','Reply','Guardianship_Date','Court',
    'Guardianship_Response_Date','Observation','Fk_Management_Type']

    def get_context_data(self,**kwargs):
        context = super(RightPetitionCreate,self).get_context_data(**kwargs)
        context['management_type'] = Management_Type.objects.all()
        context['management_typeId'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar los derechoos de peticion de los clientes
class RightPetitionView(ListView):
    model = Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_list.html'
    #context_object_name = 'derechopeticion'

    def get_context_data(self,**kwargs):
        context = super(RightPetitionView,self).get_context_data(**kwargs)
        context['derechopeticion'] = Right_Petition.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

# clase para actualziar los derechos de peticion de los clientes
class RightPetitionUpdate(UpdateView):
    model = Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_edit.html'
    fields = ['Type_Application','Line','Send_Date','Filed_Number','Reply_Date',
    'Process_State','Reply','Guardianship_Date','Court',
    'Guardianship_Response_Date','Observation','Fk_Management_Type']

    def get_context_data(self,**kwargs):
        context = super(RightPetitionUpdate,self).get_context_data(**kwargs)
        context['derechopeticion'] = Right_Petition.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')


class RightPetitionDelete(DeleteView):
    model= Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_delete.html'
    def get_success_url(self):
        return reverse('listarnomina',args=('6') )


# clase para crear los derechos de peticion
class BankAccountsCreate(CreateView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_form.html'
    fields = ['Account_Type','Number','Bank','State','Fk_Client']
    def get_context_data(self,**kwargs):
        context = super(BankAccountsCreate,self).get_context_data(**kwargs)
        context['Bank_Accounts'] = Bank_Accounts.objects.all()
        context['Client'] = Client.objects.all()
        context['clientId'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('listarcuenta')

# clase para listar los cuentas bancarias de peticion de los clientes
class BankAccountsView(ListView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_list.html'
    context_object_name = 'cuenta'
    def get_context_data(self,**kwargs):
        context = super(BankAccountsView,self).get_context_data(**kwargs)
        context['cuenta'] = Bank_Accounts.objects.filter(Fk_Client=self.kwargs['pk'])
        context['clientId'] = self.kwargs['pk']
        return context

# clase para actualziar los derechos de peticion de los clientes
class BankAccountsUpdate(UpdateView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_update.html'
    fields = ['Account_Type','Number','Bank','State','Fk_Client']
    def get_context_data(self,**kwargs):
        context = super(BankAccountsUpdate,self).get_context_data(**kwargs)
        context['cuenta'] = Bank_Accounts.objects.filter(Fk_Client=self.kwargs['pk'])
        context['clientId'] = self.kwargs['pk']
        return context


    def get_success_url(self):
        return reverse('listarcuenta')

# se crea la clase para eliminar las derechos de peticion
class BankAccountsDelete(DeleteView):
    model= Bank_Accounts
    def get_success_url(self):
        return reverse('eliminarcuenta')

# clase para crear ls desembolsos
class DisbursementCreate(CreateView):
    model = Disbursement
    template_name = 'gestionfinanciera/bank_management/disbursement_form.html'
    fields = ['Future_Value_Portfolio', 'Payment_Value', 'Banking_Entity',
    'Pay_Date','Disbursement_Amount','Number_Installment','Disbursement_Value',
    'Adviser','State','Fk_Management_Type']

    def get_context_data(self,**kwargs):
        context = super(DisbursementCreate,self).get_context_data(**kwargs)
        context['management_type'] = Management_Type.objects.all()
        context['management_typeId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar los deembolsos de peticion de los clientes
class DisbursementView(ListView):
    model = Disbursement
    template_name = 'gestionfinanciera/bank_management/disbursement_list.html'
    #context_object_name = 'desembolso'

    def get_context_data(self,**kwargs):
        context = super(DisbursementView,self).get_context_data(**kwargs)
        context['desembolso'] = Disbursement.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

# clase para actualziar los Desembolsos de los clientes
class DisbursementUpdate(UpdateView):
    model = Disbursement
    template_name = 'gestionfinanciera/bank_management/disbursement_edit.html'

    fields = ['Future_Value_Portfolio', 'Payment_Value', 'Banking_Entity',
    'Pay_Date','Disbursement_Amount','Number_Installment','Disbursement_Value',
    'Adviser','State','Fk_Management_Type']
    def get_context_data(self,**kwargs):
        context = super(DisbursementUpdate,self).get_context_data(**kwargs)
        context['desembolso'] = Disbursement.objects.filter(Fk_Management_Type=self.kwargs['pk'])
        context['management_typeId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# se crea la clase para eliminar las desembolsos
class DisbursementDelete(DeleteView):
    model= Disbursement
    template_name = 'gestionfinanciera/bank_management/disbursement_delete.html'
    def get_success_url(self):
        return reverse('listarcliente')

#clase para crear la simluacion bancaria
class SimulationBankingCreate(CreateView):
    model = Simulation_Banking
    template_name = 'gestionfinanciera/bank_management/simulation_banking_form.html'

    fields = ['Bank', 'Number_Quotas', 'Factor', 'Estimed_Credit',
    'Quota_Value','Fk_Client_Payroll']
    def get_context_data(self,**kwargs):
        context = super(SimulationBankingCreate,self).get_context_data(**kwargs)
        context['Payroll_Client'] = Payroll_Client.objects.all()
        context['payrollId'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('editarcliente')

# clase para listar las simulaciones bancariaas de los clientes
class SimulationBankingView(ListView):
    model = Simulation_Banking
    template_name = 'gestionfinanciera/bank_management/simulation_banking_list.html'

    def get_context_data(self,**kwargs):
        context = super(SimulationBankingView,self).get_context_data(**kwargs)
        context['simulacion'] = Simulation_Banking.objects.filter(Fk_Client_Payroll=self.kwargs['pk'])
        context['payrollId'] = self.kwargs['pk']
        return context

# clase para actualizar la simulacion bancaria
class SimulationBankingUpdate(UpdateView):
    model = Simulation_Banking
    #context_object_name = 'nomina'
    template_name = 'gestionfinanciera/bank_management/simulation_banking_edit.html'
    fields= ['Bank', 'Number_Quotas', 'Factor', 'Estimed_Credit',
    'Quota_Value','Fk_Client_Payroll']

    def get_context_data(self,**kwargs):
        context = super(SimulationBankingUpdate,self).get_context_data(**kwargs)
        context['simulacion'] = Payroll_Client.objects.filter(Fk_Client=self.kwargs['pk'])
        context['nomina'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('listarnomina')



'''def Client(request):
    template_name = 'client_form.html'
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    return render(request, template_name, {'form':form})'''

'''def crear_cliente(request):
    if request.method == "POST":
        Client.objects.create()
    return render(request, "")'''

# se crea la funcion la cual valida la informacion que llega del formulari

def Reference(request):
    template_name = 'crear_referencia.html'
    form = ReferenciaForm()

    if request.method ==  'POST':
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    return render(request, template_name, {'form':form})



# recupera o cre uninstancia de logging
logger = logging.getLogger(__name__)
