from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from shop.models import Product


class UserLoginForm(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True, initial=False,
                    widget=forms.PasswordInput)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'