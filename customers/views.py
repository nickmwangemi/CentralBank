from django.shortcuts import render,redirect
from .models import Customer
from accounts.models import Account
from transactions.models import Deposit,Withdrawal,MoneyTransfer
from django.contrib import messages


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
    current_balance = account.balance
    new_balance = current_balance

    if request.method == "POST":
        form = request.POST
        deposit = Deposit()
        deposit.amount =  float(form['amount'])
        deposit.save()

        account = Account()
        account.balance = Account.objects.get(pk=pk)
        new_balance = current_balance + deposit.amount
        account.balance = new_balance 
        print(new_balance)
        
        account.save()
        
        deposit.customer = Customer.objects.get(pk=pk)
        deposit.save()
        

        customer = Customer.objects.get(pk=pk)
        messages.success(request, 'You have just made a deposit of Ksh. {}. \n Your new balance is Ksh. {}'.format(deposit.amount,new_balance))
    

        return redirect('customers:deposit_detail',customer.pk)
    
    
    account = Account.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    deposit = Deposit.objects.get(pk=pk)
   
    
    context = {
        'current_balance':current_balance,
        'account':account,
        'customer': customer,
        'deposit':deposit,  
    }
    return render(request,'customers/deposit.html',context)



def deposit_detail(request,pk):
    deposit = Deposit.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    deposits = Customer.objects.all()
    
    context = {
        'deposit':deposit,
        'customer':customer, 
        'account':account,  
        'deposits':deposits,
    }


    return render(request,'customers/deposit_detail.html',context)



def withdraw(request,pk):
    if request.method == "POST":
        form = request.POST
        withdraw = Withdrawal()
        withdraw.amount =  form['amount']
        withdraw.customer = Customer.objects.get(pk=pk)
        withdraw.save()
        
        customer = Customer.objects.get(pk=pk)
        messages.success(request, 'You have made a withdrawal of Ksh. {}'.format(withdraw.amount))


        return redirect('customers:withdraw',customer.pk)

    account = Account.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    deposit = Deposit.objects.get(pk=pk)
    
    context = {
        'account':account,
        'customer': customer,
        'deposit':deposit,
         
        
    }
    return render(request,'customers/withdraw.html',context)






def edit_details(request,pk):
    customer = Customer.objects.get(pk=pk)
    context = {
        'customer': customer,
    
    }

    return render(request,'customers/edit_details.html',context)
