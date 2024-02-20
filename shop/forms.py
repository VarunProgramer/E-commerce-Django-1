from.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form_input', 'placeholder' : 'username'})),
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form_input'})),
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form_input'})),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form_input'})),
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']