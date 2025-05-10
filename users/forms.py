from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1',]
class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['leetcode','github','photo','bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'hidden'})