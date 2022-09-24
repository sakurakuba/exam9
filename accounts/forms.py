from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'First name', 'last_name': 'Last Name', 'email': 'Email'}



