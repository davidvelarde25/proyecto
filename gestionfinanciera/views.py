from django.shortcuts import render
#from django.http import HttpResponseRedirect
from .models import (Client, Reference,Simulation_Banking,Customer_Referrer,
 Management_Type,Advisor_Records, Certificate,Payroll_Client, Reference,
 Financial_Obligation, Right_Petition, Bank_Accounts,Disbursement,Actual_State)
from django.contrib.auth.models import User
from django.urls import reverse
# vistas basadas en clase
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
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

# funcion para traer loss aesores registrados en la base de datos
'''def Advisor_Records(request):
    Advisor_Records = Advisor_Records.objects.all()
    contex= {"clientes" : Advisor_Records }
    return render(request, "client_list.html", context)
'''

# clase para listar los clientes
class ClientView(ListView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_list.html'
    context_object_name = 'clientes'

'''
# clase para listar los asesores
class AdvisorRecordsView(ListView):
    model = Advisor_Records
    #template_name = 'gestionfinanciera/management_type_form.html'
    context_object_name = 'clientes'
'''
# clase para crear los clientes
class ClientCreate(CreateView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_form.html'
    fields = ['Name', 'Identification', 'Email','Address','City','Cell_Phone',
    'Phone', 'Date_of_birth','Stratum','Neighborhood']
    #fields = ['_all_']
    def get_success_url(self):
        return reverse('index')

# clase para actualziar los clientes
class ClientUpdate(UpdateView):
    model = Client
    template_name = 'gestionfinanciera/Client/client_edit.html'
    fields = ['Name', 'Identification', 'Email','Address','City','Cell_Phone',
    'Phone', 'Date_of_birth','Stratum','Neighborhood']

    def get_success_url(self):
        return reverse('index')

# clase para crear el tipo de gestion de un usuario
class ManagementTypeCreate(CreateView):
    model = Management_Type
    #template_name = 'Templates/gestionfinanciera/client_form.html'
    fields = '__all__'

     #se sobreescribe este método para obtener información de otros modelos
    def get_context_data(self,**kwargs):
        context = super(ManagementTypeCreate,self).get_context_data(**kwargs)
        context['customer_referrer'] = Customer_Referrer.objects.all()
        context['advisor_records'] = Advisor_Records.objects.all()
        context['actual_state'] = Actual_State.objects.all()

        return context
    def get_success_url(self):
        return reverse('')

# clase para listar la gestion que se le va a realziar al cliente
class ManagementTypeList(ListView):
    model = Management_Type
    template_name = 'gestionfinanciera/management_type_list.html'
    context_object_name = 'tipogestion'

# clase para actualizar el tipo de gestion de un usuario
class ManagementTypeUpdate(UpdateView):
    model = Management_Type
    template_name = 'gestionfinanciera/management_type_update.html'
    fields = '__all__'

     #se sobreescribe este método para obtener información de otros modelos
    def get_context_data(self,**kwargs):
        context = super(ManagementTypeUpdate,self).get_context_data(**kwargs)
        context['customer_referrer'] = Customer_Referrer.objects.all()
        context['advisor_records'] = Advisor_Records.objects.all()
        context['actual_state'] = Actual_State.objects.all()

        return context
    def get_success_url(self):
        return reverse('')

# clase para listar la gestionde un cliente
'''class ManagementTypeCreate(ListView):
    model = Management_Type
    template_name = 'gestionfinanciera/Client/payroll_client_list.html'
    context_object_name = 'nomina'
'''

# clase para crear el la nomina del cliente
class PayrollClientCreate(CreateView):
    model = Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_form.html'
    fields=['Payroll_Company', 'Payroll_Type', 'Salary_Value','Permanent_Income','Social_Security','Law_Applies','Permanent_Discounts', 'Non_Concellable_Value','Payment_Capacity','Bonding_Date','Fk_Client']
    def get_context_data(self,**kwargs):
        context = super(PayrollClientCreate,self).get_context_data(**kwargs)
        context['client'] = Client.objects.all()

        return context

    def get_success_url(self):
        return reverse('index')

# clase para listar las nominas de los clientes
class PayrollClientView(ListView):
    model = Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_list.html'
    context_object_name = 'nomina'

    #nominas = Payroll_Client.objects.filter(Fk_Client=)
    def get_context_data(self,**kwargs):
        context = super(PayrollClientView,self).get_context_data(**kwargs)
        context['client'] = Client.objects.all()

        return context

# clase para actualziar las referencias de los clientes
class PayrollClientUpdate(UpdateView):
    model = Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_edit.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('listarnomina')

# se crea la clase para eliminar las referencias
class PayrollClientDelete(DeleteView):
    model= Payroll_Client
    template_name = 'gestionfinanciera/Client/payroll_client_form.html'
    def get_success_url(self):
        return reverse('listarnomina')

# clase para crear las referencias del cliente
class ReferenceCreate(CreateView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar las referencias de los clientes
class ReferenceView(ListView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_list.html'
    context_object_name = 'referencia'

# clase para actualziar las referencias de los clientes
class ReferenceUpdate(UpdateView):
    model = Reference
    template_name = 'gestionfinanciera/Client/reference_edit.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')

# se crea la clase para eliminar las referencias
class ReferenceDelete(DeleteView):
    model= Reference
    def get_success_url(self):
        return reverse('listarreferencia')

# clase para crear las obligaciones de los clientes
class FinancialObligationCreate(CreateView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar las referencias de los clientes
class FinancialObligationView(ListView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_list.html'
    context_object_name = 'obligacion'

# clase para actualziar las referencias de los clientes
class FinancialObligationUpdate(UpdateView):
    model = Financial_Obligation
    template_name = 'gestionfinanciera/obligation/financial_obligation_edit.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# se crea la clase para eliminar las referencias
class FinancialObligationDelete(DeleteView):
    model= Financial_Obligation
    def get_success_url(self):
        return reverse('listarobligacion')


# clase para crear el certificado
class CertificateCreate(CreateView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar los certifiados de los clientes
class CertificateView(ListView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_list.html'
    context_object_name = 'certificado'

# clase para actualziar los certificados de los clientes
class CertificateUpdate(UpdateView):
    model = Certificate
    template_name = 'gestionfinanciera/obligation/certificate_edit.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('actualizarcertificado')

# se crea la clase para eliminar las certificados
class CertificateDelete(DeleteView):
    model= Certificate
    def get_success_url(self):
        return reverse('eliminarcertificado')

# clase para crear los derechos de peticion
class RightPetitionCreate(CreateView):
    model = Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar los derechoos de peticion de los clientes
class RightPetitionView(ListView):
    model = Right_Petition
    template_name = 'gestionfinanciera/obligation/right_petition_list.html'
    context_object_name = 'derechopeticion'

# clase para actualziar los derechos de peticion de los clientes
class RightPetitionUpdate(UpdateView):
    model = Right_Petition
    fields = '__all__'
    def get_success_url(self):
        return reverse('actualizarderechopeticion')

# se crea la clase para eliminar las derechos de peticion
class RightPetitionDelete(DeleteView):
    model= Right_Petition
    def get_success_url(self):
        return reverse('eliminarderechopeticion')


# clase para crear los derechos de peticion
class BankAccountsCreate(CreateView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar los cuentas bancarias de peticion de los clientes
class BankAccountsView(ListView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_list.html'
    context_object_name = 'cuenta'

# clase para actualziar los derechos de peticion de los clientes
class BankAccountsUpdate(UpdateView):
    model = Bank_Accounts
    template_name = 'gestionfinanciera/bank_management/bank_accounts_update.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('actualizarcuenta')

# se crea la clase para eliminar las derechos de peticion
class BankAccountsDelete(DeleteView):
    model= Bank_Accounts
    def get_success_url(self):
        return reverse('eliminarcuenta')

# clase para crear ls desembolsos
class DisbursementCreate(CreateView):
    model = Disbursement
    #template_name = 'Templates/gestionfinanciera/client_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')

# clase para listar los deembolsos de peticion de los clientes
class DisbursementView(ListView):
    model = Disbursement
    #template_name = 'gestionfinanciera/listarobligacion.html'
    context_object_name = 'desembolso'

# clase para actualziar los Desembolsos de los clientes
class DisbursementUpdate(UpdateView):
    model = Disbursement
    fields = '__all__'
    def get_success_url(self):
        return reverse('actualizardesembolso')

# se crea la clase para eliminar las desembolsos
class DisbursementDelete(DeleteView):
    model= Disbursement
    def get_success_url(self):
        return reverse('eliminardesembolso')

class SimulationBankingCreate(CreateView):
    model = Simulation_Banking
    #template_name = 'Templates/gestionfinanciera/client_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('')


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
