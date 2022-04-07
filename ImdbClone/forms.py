from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height: 40px;border-radius: 5px;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height: 40px;border-radius: 5px;',
                'placeholder': 'Email'
            }),
            'password1': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height: 40px;border-radius: 5px;',
                'placeholder': 'Email'
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height: 40px;border-radius: 5px;',
                'placeholder': 'Email'
            }),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
