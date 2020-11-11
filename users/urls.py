from django.contrib import admin
from django.urls import path, include
from gestionfinanciera import views
from users.views import ListUsers

from .views import signup, ActivateUser, templateEmailSent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userslist/', ListUsers.as_view(), name="userslist"),
    #Activar cuenta nuevo registro
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
]
