
from django.contrib import admin
from django.urls import path, include
from gestionfinanciera import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),# ruta pra mostrar los clientes registrados
    #path('listarcliente/', views.index, name="listarcliente"),# ruta pra mostrar los clientes registrados
    path('admin/', admin.site.urls),
    path('crearcliente/', views.ClientCreate.as_view(), name="crearcliente"), # ruta para crear nuevos clientes
    #path('editarcliente/<int:pk>/', views.ClientUpdate.as_view(), name="editarcliente"), # ruta para actualizar un cliente especifico
    path('listarcliente/', views.ClientView.as_view(), name= 'listarcliente'),# ruta pra mostrar las nominas de cada clientes
    path('editarcliente/<int:pk>/', views.ClientUpdate.as_view(), name='editarcliente'), # ruta para actualizar un cliente especifico

    path('creargestion/', views.ManagementTypeCreate.as_view(), name="creargestion"), # ruta para crear la gestion de un cliente
    path('listargestion/', views.ManagementTypeView.as_view(), name="listargestion"), # ruta para crear la gestion de un cliente
    path('editargestion/<int:pk>/', views.ManagementTypeUpdate.as_view(), name="editargestion"), # ruta para crear la gestion de un cliente

    path('crearnomina/', views.PayrollClientCreate.as_view(), name="crearnomina"), # ruta para crear la nomina del cliente
    path('listarnomina/', views.PayrollClientView.as_view(), name= 'listarnomina'),# ruta pra mostrar las nominas de cada clientes
    path('editarnomina/<int:pk>/', views.PayrollClientUpdate.as_view(), name="editarnomina"), # ruta para actualizar la nomina del cliente
    path('eliminarnomina/<int:pk>/', views.PayrollClientDelete.as_view(), name='eliminarnomina'),# ruta para elimiar las referncia

    path('crearreferencia/', views.ReferenceCreate.as_view(), name="crearreferencia"), # ruta para crear las referencias de los cliente
    path('listarreferencia/', views.ReferenceView.as_view(), name= 'listarreferencia'),# ruta pra mostrar las referencias registrados de cada cliente
    path('editarreferencia/<int:pk>/', views.ReferenceUpdate.as_view(), name="editarreferencia"), # ruta para actualizar una refferencia del cliente
    path('eliminarreferencia/<int:pk>/', views.ReferenceDelete.as_view(), name='eliminarreferencia'),# ruta para eliminar las refrencias

    path('crearobligacion/', views.FinancialObligationCreate.as_view(), name="crearobligacion"), # ruta para crear las obligaciones de los clientes
    path('listarobligacion/', views.FinancialObligationView.as_view(), name= 'listarobligacion'),# ruta pra mostrar las Obligaciones registrados de cada cliente
    path('editarobligacion/<int:pk>/', views.FinancialObligationUpdate.as_view(), name="editarobligacion"), # ruta para Obligaciones una refferencia del cliente
    path('eliminarobligacion/<int:pk>/', views.FinancialObligationDelete.as_view(), name='eliminarobligacion'),# ruta para eliminar las obligaciones

    path('crearcertificado/', views.CertificateCreate.as_view(), name="crearcertificado"), # ruta para crear el certificado de cada na de las obligaciones
    path('listarcertificado/', views.CertificateView.as_view(), name= 'listarcertificado'),# ruta pra mostrar las certificados registrados de cada cliente
    path('editarcertificado/<int:pk>/', views.CertificateUpdate.as_view(), name="editarcertificado"), # ruta para certificados una refferencia del cliente
    path('eliminarcertificado/<int:pk>/', views.CertificateDelete.as_view(), name='eliminarcertificado'),# ruta para eliminar las certificados

    path('crearderechopeticion/', views.RightPetitionCreate.as_view(), name="crearderechopeticion"), # ruta para crear el certificado de cada na de las obligaciones
    path('listarderechopeticion/', views.RightPetitionView.as_view(), name= 'listarderechopeticion'),# ruta pra mostrar las derechos de peticion registrados de cada cliente
    path('editarderechopeticion/<int:pk>/', views.RightPetitionUpdate.as_view(), name="editarderechopeticion"), # ruta para editar los datos de los derechos de peticion de un cliente
    path('eliminarderechopeticion/<int:pk>/', views.RightPetitionDelete.as_view(), name='eliminarderechopeticion'),# ruta para eliminar las derechos de peticion de un cliente

    path('crearcuenta/', views.BankAccountsCreate.as_view(), name="crearcuenta"), # ruta para crear las cuentas bancarias de los clientes
    path('listarcuenta/', views.BankAccountsView.as_view(), name= 'listarcuenta'),# ruta pra mostrar las derechos de peticion registrados de cada cliente
    path('editarcuenta/<int:pk>/', views.BankAccountsUpdate.as_view(), name="editarcuenta"), # ruta para editar los datos de los derechos de peticion de un cliente
    path('eliminarcuenta/<int:pk>/', views.BankAccountsDelete.as_view(), name='eliminarcuenta'),# ruta para eliminar las derechos de peticion de un cliente

    path('creardesembolso/', views.DisbursementCreate.as_view(), name="creardesembolso"), # ruta para crear las desembolsos  de los clientes
    path('listardesembolso/', views.DisbursementView.as_view(), name= 'listardesembolso'),# ruta pra mostrar las desembolsos registrados de cada cliente
    path('editardesembolso/<int:pk>/', views.DisbursementUpdate.as_view(), name="editardesembolso"), # ruta para editar los datos de los desembolsos de un cliente
    path('eliminardesembolso/<int:pk>/', views.DisbursementDelete.as_view(), name='eliminardesembolso'),# ruta para eliminar las desembolsos de un cliente

    path('crearsimulacion/', views.SimulationBankingCreate.as_view(), name="crearsimulacion"), # ruta para crear la simulacion bancaria de los clientes
    path('listarsimulacion/', views.SimulationBankingView.as_view(), name= 'listarsimulacion'),# ruta pra mostrar las desembolsos registrados de cada cliente
    path('editardesembolso/<int:pk>/', views.DisbursementUpdate.as_view(), name="editardesembolso"), # ruta para editar los datos de los desembolsos de un cliente
    path('eliminardesembolso/<int:pk>/', views.DisbursementDelete.as_view(), name='eliminardesembolso'),# ruta para eliminar las desembolsos de un cliente



    #path('estion_cliente/', views.gestion_cliente, name="gestion_cliente"), # ruta para crear nuevos clientes
    path('accounts/', include('django.contrib.auth.urls')),
    #path('users/', include(('users.urls','users'), namespace='users')),


]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
