from django.shortcuts import render
from .models import Customer
from accounts.models import Account
from transactions.models import Deposit,Withdrawal,MoneyTransfer

# Create your views here.
def account_status(request,pk):
    # get current user
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    deposits = Deposit.objects.filter(pk=pk)
    withdrawals = Withdrawal.objects.filter(pk=pk)
    money_transfers = MoneyTransfer.objects.filter(pk=pk)

    context = {
        'customer': customer,
        'account': account,
        'deposits':deposits,
        'withdrawals':withdrawals,
        'money_transfers':money_transfers,
    }



    return render(request,'customers/account_status.html',context)

def money_transfer(request,pk):
    # get current user
    customer = Customer.objects.get(pk=pk)
    accounts = Account.objects.all()
    
    if request.method == "POST":
        form = request.POST
        account_number = form['account_number']
        amount = form['amount']
       
        return redirect('customers:money_transfer',customer.pk)
    
    # Status.objects.get(username=request.user)
    context = {
        'customer': customer,
        'accounts':accounts
    }

    return render(request,'customers/money_transfer.html',context)


def deposit(request,pk):
    account = Account.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    accounts = Account.objects.all()
    

    context = {
        'account':account,
        'customer': customer,
        'accounts':accounts,
        
    }

    return render(request,'customers/deposit.html',context)

def withdraw(request,pk):
    account = Account.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    accounts = Account.objects.all()
    context = {
        'account':account,
        'customer': customer,
        'accounts':accounts,
        
    }

    return render(request,'customers/withdraw.html',context)

def edit_details(request,pk):
    customer = Customer.objects.get(pk=pk)
    context = {
        'customer': customer,
    
    }

    return render(request,'customers/edit_details.html',context)
