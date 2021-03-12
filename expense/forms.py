from django import forms
from django.forms import ModelForm
from .models import *


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['title','amount','date','category']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})}


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['title', 'amount', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})}


class StartForm(forms.ModelForm):

    class Meta:
        model = StartAmt
        fields = {'amount'}
