from django.contrib import admin
from django.urls import path, include
#importación librerias
from gestionfinanciera import views
from users.views import ListUsers

urlpatterns = [
    path('crear/', views.crear_cliente, name='crear'),
    #path('users/', include('users.urls', 'users')),
    #path('userslist/', ListUsers.as_view(), name= "userlist")

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
