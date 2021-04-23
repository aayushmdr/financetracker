from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Password',
        }
    ))


class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'First name',
        }
    ))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Last name',
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Enter username here..',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Enter email here..',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
                                                                  'placeholder': 'Enter password..',
                                                                  'id': 'exampleInputPassword',
                                                                  }))
    password2 = forms.CharField(label="Repeat password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
                                                                  'placeholder': 'Repeat password..',
                                                                  'id': 'exampleRepeatPassword',
                                                                  }))

    class Meta:
        model = User
        fields = ['firstname','lastname','username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True})
        }


