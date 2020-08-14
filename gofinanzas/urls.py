
from django.contrib import admin
from django.urls import path, include
#importación librerias
from gestionfinanciera import views
from users.views import ListUsers

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('crear_cliente/', views.ClientCreate.as_view(), name="crear_cliente"), # ruta para crear nuevos clientes
    path('editar/<int:pk>/', views.BadgetUpdate.as_view(), name="editar"), # ruta para crear nuevos clientes
    #path('estion_cliente/', views.gestion_cliente, name="gestion_cliente"), # ruta para crear nuevos clientes

    path('accounts/', include('django.contrib.auth.urls')),
    #path('users/', include('users.urls', 'users')),
    #path('userslist/', ListUsers.as_view(), name= "userlist")
    #path('', include('gestionfinanciera.urls'))
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
