import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, widgets
from .models import *





class ExpenseFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    start_date = DateFilter(field_name="date", lookup_expr='gte', label='Start date')
    end_date = DateFilter(field_name="date", lookup_expr='lte', label='End date')
    amount_greater_than = NumberFilter(field_name='amount', lookup_expr='gt', label='Amount more than')
    amount_lesser_than = NumberFilter(field_name='amount', lookup_expr='lt', label='Amount less than')
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user','amount','title','date','image']




class IncomeFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    start_date = DateFilter(field_name="date", lookup_expr='gte', label='Start date' )
    end_date = DateFilter(field_name="date", lookup_expr='lte', label='End date')
    amount_greater_than = NumberFilter(field_name='amount', lookup_expr='gt', label='Amount more than')
    amount_lesser_than = NumberFilter(field_name='amount', lookup_expr='lt', label='Amount less than')
    class Meta:
        model = Income
        fields = '__all__'
        exclude = ['user','amount','title','date','image']
