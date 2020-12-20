from django import forms
from django.forms import ModelForm
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    class Meta:
       model= Producto
       fields = ["nombre", "precio", "descripcion", "nuevo", "marca", "fecha_fabricacion",  "imagen"]   
       
       widget = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
       
class ContactoForm(ModelForm):
   # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "mensaje", "tipo_consulta"]
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'
        exclude = ["is_superuser", "password", "date_joined", "last_login","is_active", "is_staff", ]