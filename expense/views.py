from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .filters import *




def login_success(request):

    samt = StartAmt.objects.filter(user=request.user)
    if not samt:

        return redirect('start')
    else:
        return redirect('home')


@login_required()
def start(request):
    if request.method=='POST':
        form = StartForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = StartForm()
    return render(request, 'expense/start.html', {'form': form})

@login_required()
def index(request):
    balance = ''
    difference = ''
    expenses = Expense.objects.filter(user = request.user)
    all_incomes = Income.objects.filter(user = request.user)
    startamt = StartAmt.objects.filter(user = request.user)
    firstFiveexp = Expense.objects.filter(user = request.user).order_by('-date')[:5]
    firstFiveinc = Income.objects.filter(user = request.user).order_by('-date')[:5]

    sum = 0
    a=0
    for expense in expenses:
        sum += expense.amount

    Incomesum = 0
    for income in all_incomes:
        Incomesum += income.amount

    for bal in startamt:
        a = bal.amount

    if a>0:
        balance = (a+Incomesum)-sum
        difference = sum-(Incomesum+a)


    context = {
        'expenses':expenses,
        'incomes': all_incomes,
        'totalexp':sum,
        'totalIncome':Incomesum,
        'diff':difference,
        'firstFiveexp':firstFiveexp,
        'firstFiveinc':firstFiveinc,
        'balance':balance,
        'start':startamt,


    }
    return render(request,'expense/index.html',context)

@login_required()
def expenseDetail(request):
    expenses = Expense.objects.filter(user = request.user).order_by('-date')
    categories = Category.objects.all()

    myFilter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = myFilter.qs

    list1 = []
    catlist = []
    b=1
    sum=0
    for cat  in categories:
        cat1 = Expense.objects.filter(category=b,user = request.user)
        cat2 = Category.objects.get(id=b)
        catlist.append(cat2)
        for cat in cat1:
            sum += cat.amount

        list1.append(sum)
        sum = 0
        b += 1

    context = {
        'expenses': expenses,
        'sum':sum,
        'categories':categories,
        'list':list1,
        'catlist':catlist,
        'myFilter' : myFilter

    }
    return render(request, 'expense/expensesdetail.html', context)

@login_required()
def detailExpense(request, pk):
    expense = Expense.objects.get(id = pk)

    context = {
        'expense': expense,


    }
    return render(request, 'expense/expensedetail.html', context)

@login_required()
def addExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('all_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expense/addexpense.html',{'form':form, 'catform': AddCategoryForm})

def addCategory(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('add_expense')
        else:
            form = AddCategoryForm()
        return render(request, 'expense/addexpense.html', {'catform': AddCategoryForm})

def updateExpense(request, pk):
    expense = Expense.objects.get(id = pk)
    form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
        return redirect('all_expenses')

    context ={
        'form':form
    }
    return render(request, 'expense/update_expense.html',context)


def deleteExpense(request, pk):
    expense = Expense.objects.get(id = pk)
    if request.method=='POST':
        expense.delete()
        messages.success(request, 'Item deleted!')
        return redirect('all_expenses')
    context ={
        'expense':expense
    }
    return render(request, 'expense/delete.html', context)

@login_required()
def detailIncome(request, pk):
    income = Income.objects.get(id = pk)

    context = {
        'income': income,


    }
    return render(request, 'expense/single_income.html', context)

def incomeDetail(request):
    incomes = Income.objects.filter(user = request.user)
    categories = IncomeCategory.objects.all()

    myFilter = IncomeFilter(request.GET, queryset=incomes)
    incomes = myFilter.qs

    context = {
        'incomes': incomes,
        'myFilter' : myFilter
    }
    return render(request, 'expense/incomedetail.html', context)

@login_required()
def addIncome(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('all_incomes')
    else:
        form = IncomeForm()
    return render(request, 'expense/addincome.html',{'form':form})

@login_required()
def updateIncome(request, pk):
    income = Income.objects.get(id = pk)
    form = IncomeForm(instance=income)

    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
        return redirect('all_incomes')

    context ={
        'form':form
    }
    return render(request, 'expense/update_income.html',context)

@login_required()
def deleteIncome(request, pk):
    income = Income.objects.get(id = pk)
    if request.method=='POST':
        income.delete()
        messages.success(request, 'Item deleted!')
        return redirect('all_incomes')
    context ={
        'income':income
    }
    return render(request, 'expense/income_delete.html', context)