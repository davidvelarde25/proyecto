
from django.contrib import admin
from django.urls import path, include
#importación librerias
from gestionfinanciera import views
from users.views import ListUsers

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('users/', include('users.urls', 'users')),
    #path('userslist/', ListUsers.as_view(), name= "userlist")
    path('', include('gestionfinanciera.urls'))
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
