from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(IncomeCategory)
admin.site.register(StartAmt)