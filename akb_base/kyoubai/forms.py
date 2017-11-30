
from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

class BidForm(forms.Form):
    amount = forms.DecimalField(label='Betrag', max_digits=15, decimal_places=2, widget=forms.NumberInput)