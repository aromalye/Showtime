from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'email', 'location', 'first_name', 'last_name', 'phone_number']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
