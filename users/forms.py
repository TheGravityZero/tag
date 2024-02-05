from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-file__input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-file__input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-file__input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-file__input'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-file__input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')