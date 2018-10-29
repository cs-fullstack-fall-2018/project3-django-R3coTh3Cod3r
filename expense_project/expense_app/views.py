from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ExpenseModel
from .forms import FormsForm, UserForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    expense_list = ExpenseModel.objects.all()
    content = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html',content)

@login_required
def expenseList(request):
    expense_list = ExpenseModel.objects.filter(foreign_expense_user=request.user)
    content = {'expense_list': expense_list}
    return render(request, 'expense_app/index.html', content)

def makeUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #post=form.save(commit=False)
            #post.foreign_expense_user=request.user
            User.objects.create_user(request.POST.get("name"), "",request.POST.get("password"))
            #post.save()
        return redirect('index')
    else:
        form = UserForm()
        return render(request, 'expense_app/createUser.html',{'form': form})

def create(request):
    if request.method == 'POST':
        form = FormsForm(request.POST)
        changeForm = form.save(commit=False)
        changeForm.testUser = request.user
        changeForm.save()
        return redirect('index')

    else:
        form = FormsForm()
        return render(request, 'expense_app/homev2.html', {'form':form})

@login_required
def login_view(request):
    logged_in_user= authenticate(username=request.POST.get("name"),)
    login(request,logged_in_user)

def database(request):
    if request.method == 'POST':
        form = ExpenseModel(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get('username'), "", request.POST.get('foreign_expense_user'),"",request.POST.get('balance'),"",request.POST.get('emergency_fund_status'),"",request.POST.get('withdrawls'),"",request.POST.get('deposit'),"",request.POST.get('amount'),"",request.POST.get('statedDate'))
            return redirect('index')
        else:
            form = ExpenseModel()
            return render(request,'expense_app/database.html',{'form':form})