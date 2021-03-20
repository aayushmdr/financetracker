from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('start/',views.start, name= 'start'),
    path('all_expenses/',views.expenseDetail, name= 'all_expenses'),
    path('addexpense/',views.addExpense, name= 'add_expense'),
    path('update_exp/<str:pk>', views.updateExpense, name="update_expense"),
    path('delete_exp/<str:pk>', views.deleteExpense, name="delete_expense"),
    path('detail_exp/<str:pk>', views.detailExpense, name="detail_expense"),

    path('addIncome/',views.addIncome, name= 'add_income'),
    path('all_incomes/',views.incomeDetail, name= 'all_incomes'),
    path('update_income/<str:pk>', views.updateIncome, name="update_income"),
    path('delete_income/<str:pk>', views.deleteIncome, name="delete_income"),
    path('detail_income/<str:pk>', views.detailIncome, name="detail_income"),

    path('login_success/', views.login_success, name='login_success')
]