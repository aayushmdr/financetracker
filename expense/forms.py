from django import forms
from django.forms import ModelForm
from .models import *


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'category', 'description', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form control-user'}),
            'title': forms.TextInput(attrs={'class': 'form-control form control-user'}),
            'amount': forms.TextInput(attrs={'class': 'form-control form control-user'}),
            'category': forms.Select(attrs={'class': 'form-control form control-user'}),
            'description': forms.Textarea(attrs={'class': 'form-control form control-user'}),

        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['title', 'amount', 'date', 'category', 'description', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form control-user'}),
            'title': forms.TextInput(attrs={'class': 'form-control form control-user'}),
            'amount': forms.TextInput(attrs={'class': 'form-control form control-user'}),
            'category': forms.Select(attrs={'class': 'form-control form control-user'}),
            'description': forms.Textarea(attrs={'class': 'form-control form control-user'}),


        }


class StartForm(forms.ModelForm):
    class Meta:
        model = StartAmt
        fields = {'amount'}
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-user'})
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {'name'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }