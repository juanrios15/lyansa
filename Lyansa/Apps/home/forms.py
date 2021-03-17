from django import forms
from django.core import validators
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput"
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput2"
            }
        )
    )
    first_name = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput3"
            }
        )
    )
    last_name = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput4"
            }
        )
    )
    password1 = forms.CharField(
        label='Username',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput5"
            }
        )
    )
    password2 = forms.CharField(
        label='Username',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id':"floatingInput6"
            }
        )
    )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')
            
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


####

class LoginForm(forms.Form):
    
    username = forms.CharField(
        label="Nombre de usuario", 
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario',
            }
        ))
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
            }
        )
    )
    
    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data['username']
        password = cleaned_data['password']

        if not authenticate(username=username,password=password):
            print("error")
            raise forms.ValidationError("Los datos de usuario no son correctos")

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña Actual'
            }
        )
    )
     
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    def get_initial_for_field(self, field, field_name):
        return super().get_initial_for_field(field, field_name)
    
    asunto = forms.CharField(
        label="Asunto",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Asunto o objeto',
            }
        ))
    nombre = forms.CharField(
        label="Nombre completo",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombres y apellidos',
            }
        ))
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electronico',
            }
        ))
    verify_email = forms.EmailField(
        label="Verificacion de Email",
        required=False,
        
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Verificacion de correo electronico',
            }
        ))
    mensaje = forms.CharField(
        label= "Mensaje",
        required=True,
        widget=forms.Textarea(
             attrs={
                'class': 'form-control',
                'placeholder': 'Mensaje',
            }
        ))
    
    adjunto = forms.FileField(
        label = "Adjunte un archivo: ",
        required=False,
        widget= forms.FileInput(
            attrs={
                'class': 'form-control-file',
                'style': 'width: 50%; padding-left: 10px;'
            }
        ))
    
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput)
    

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify = all_clean_data['verify_email']
        
        if email != verify:
            raise forms.ValidationError("Verifique que su correo electronico coincida")
        
