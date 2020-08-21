
from django.contrib import admin
from django.urls import path, include
from gestionfinanciera import views

urlpatterns = [
    path('', views.ClientView.as_view(), name= 'index'),# ruta pra mostrar los clientes registrados
    path('admin/', admin.site.urls),
    path('crearcliente/', views.ClientCreate.as_view(), name="crearcliente"), # ruta para crear nuevos clientes
    path('editarcliente/<int:pk>/', views.ClientUpdate.as_view(), name='editarcliente'), # ruta para actualizar un cliente especifico
    path('creargestion/', views.ManagementTypeCreate.as_view(), name="creargestion"), # ruta para crear la gestion de un cliente
    #path('creargestion/', views.AdvisorRecordsView.as_view()), # ruta para crear la gestion de un cliente
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
    path('crearderechopeticion/', views.RightPetitionCreate.as_view(), name="crearderechopeticion"), # ruta para crear el certificado de cada na de las obligaciones
    path('crearcuentas/', views.BankAccountsCreate.as_view(), name="crearcuentas"), # ruta para crear las cuentas bancarias de los clientes
    path('creardesembolso/', views.DisbursementCreate.as_view(), name="creardesembolso"), # ruta para crear las cuentas bancarias de los clientes




    #path('estion_cliente/', views.gestion_cliente, name="gestion_cliente"), # ruta para crear nuevos clientes
    path('accounts/', include('django.contrib.auth.urls')),
    #path('users/', include(('users.urls','users'), namespace='users')),

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
