from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  django import forms
from .models import FeedBackMessage

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBackMessage
        fields = ['name', 'email', 'message']
