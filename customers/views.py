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
    deposits = Deposit.objects.filter(customer_id=pk)
    withdrawals = Withdrawal.objects.filter(customer_id=pk)
    money_transfers = MoneyTransfer.objects.filter(sender_id=pk)

    context = {
        'customer': customer,
        'account': account,
        'deposits':deposits,
        'withdrawals':withdrawals,
        'money_transfers':money_transfers,
    }
    return render(request,'customers/account_status.html',context)



def money_transfer(request,pk): 
    account = Account.objects.get(pk=pk)
    sender_balance = account.balance
    
    if request.method == "POST":
        form = request.POST
        money_transfer = MoneyTransfer()
        money_transfer.sender = account # current_user
        money_transfer.amount = float(form['amount'])

        if money_transfer.amount > account.balance:
            messages.info(request, 'Transaction failed! You have insufficient funds to transact Ksh. {}. Please top-up and try again.'.format(money_transfer.amount))
        else:
            money_transfer.recipient = Account.objects.get(pk=form['account']) # recipient
            money_transfer.mobile_number = form['mobile_number']
            money_transfer.save()
        
            new_sender_balance = sender_balance - money_transfer.amount
            account.balance = new_sender_balance 

            recipient = money_transfer.recipient
            recipient_balance = recipient.balance

            new_recipient_balance = recipient_balance + money_transfer.amount
            
            account.save()
            recipient.save()
            
            messages.success(request,'Transaction successful. Ksh. {} has been transferred to Account Number: {}. New balance is Ksh. {}'.format(money_transfer.amount,money_transfer.recipient,new_sender_balance))
        
        customer = Customer.objects.get(pk=pk)
        return redirect('customers:money_transfer_detail',customer.pk)
    
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    accounts = Account.objects.all()
    context = {
        'customer': customer,
        'account':account,
        'accounts':accounts
    }
    return render(request,'customers/money_transfer.html',context)


def money_transfer_detail(request,pk):
    customer = Customer.objects.get(pk=pk)
    accounts = Account.objects.all()
    context = {
        'customer': customer,
        'accounts':accounts
    }

    return render(request,'customers/money_transfer_detail.html',context)

def deposit(request,pk):
    account = Account.objects.get(pk=pk)
    current_balance = account.balance
    new_balance = current_balance

    if request.method == "POST":
        form = request.POST
        deposit = Deposit()
        deposit.amount =  float(form['amount'])
        deposit.account = account
        
        new_balance = current_balance + deposit.amount
        account.balance = new_balance 
        
        deposit.save()
        account.save()
        
        deposit.customer = Customer.objects.get(pk=pk)
        
        customer = Customer.objects.get(pk=pk)
        messages.success(request, 'Transaction successful. You have just made a deposit of Ksh. {} into your account. New balance is Ksh. {}'.format(deposit.amount,new_balance))
    

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
    account = Account.objects.get(pk=pk)
    current_balance = account.balance
    new_balance = current_balance

    if request.method == "POST":
        form = request.POST
        withdraw = Withdrawal()
        withdraw.amount =  float(form['amount'])
        if current_balance < withdraw.amount:
            messages.info(request, 'Transaction failed! You cannot withdraw an amount that is greater than your current balance of Ksh. {}'.format(current_balance))
        
        else:
            withdraw.save()
        
            new_balance = current_balance - withdraw.amount
            account.balance = new_balance 
            
            account.save()
            
            withdraw.customer = Customer.objects.get(pk=pk)
            withdraw.save()
            messages.success(request, 'Transaction successful. You have just made a withdrawal of Ksh. {} from your account. New balance is Ksh. {}'.format(withdraw.amount,new_balance))
        
        customer = Customer.objects.get(pk=pk)
        return redirect('customers:withdrawal_detail',customer.pk)
    
    account = Account.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    deposit = Deposit.objects.get(pk=pk)
    
    context = {
        'account':account,
        'customer': customer,
        'deposit':deposit,
    }
    return render(request,'customers/withdraw.html',context)



def withdrawal_detail(request,pk):
    withdrawal = Withdrawal.objects.get(pk=pk)
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    withdrawals = Customer.objects.all()
    
    context = {
        'withdrawal':withdrawal,
        'customer':customer, 
        'account':account,  
        'withdrawals':withdrawals,
    }
    return render(request,'customers/withdrawal_detail.html',context)


def edit_details(request,pk):
    customer = Customer.objects.get(pk=pk)
    context = {
        'customer': customer,
    
    }

    return render(request,'customers/edit_details.html',context)
