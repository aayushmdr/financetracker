from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Func


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name




class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=101)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default= datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class IncomeCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=101)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=datetime.now)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class StartAmt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
