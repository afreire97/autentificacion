from django.contrib.auth.forms import  AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Comentario, Discusion
class CustomForm(UserCreationForm):
    
    email = forms.EmailField(required=True, help_text= "Campo requerido. Introduce un email válido.")
    class Meta:
        
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Esta dirección de correo electrónico ya está en uso.")
        return email
    
    
class CustomLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}),
    )    


class DiscusionForm(forms.ModelForm):
    
    class Meta:
        model = Discusion
        fields = ("titulo",)
