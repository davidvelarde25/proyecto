from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Client

# se crea la clase para el formulario de cliente
'''class ClienteForm(forms.ModelForm):
    class Meta:
        model = Client
<<<<<<< HEAD
<<<<<<< HEAD
        field = '__all__'
=======
        fields = '__all__' '''
=======

'''
>>>>>>> 0065207d0f3b14e984d2a7f78781e2f7e06719cd


# se crea el formulario para registrar los nuevos usuarios
class SgnupForm(UserCreationForm):
    username = forms.CharField(max_length=150 , label="Nombre de Usuario",
                                widget = forms.TextInput(attrs = {'class':'form-control'}))
    eamil = forms.EmailField(max_length=200 , label="Correo Electrónico",
                                widget = forms.TextInput(attrs = {'class':'form-control'}))
    password1 = forms.CharField(max_length=150 , label="Contraseña",
                                widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(max_length=150 , label="Confirme la Contraseña ",
                                widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
