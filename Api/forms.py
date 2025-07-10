from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
