from msilib.schema import Class
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usúario')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)