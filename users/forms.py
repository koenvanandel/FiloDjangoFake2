from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

#class LoginForm(AuthenticationForm):

    # username = forms.CharField(widget=forms.TextInput())
    # password = forms.CharField(widget=forms.PasswordInput())

class CustomAuthenticationForm(AuthenticationForm):
    #username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username:
            self.cleaned_data['email'] = username
        return cleaned_data
