from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'digite seu nome'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input','placeholder':'digite sua senha'}))