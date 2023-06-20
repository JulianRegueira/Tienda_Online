from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=200, help_text='')

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
        ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email"
        ]
        help_texts =  {k: "" for k in fields}