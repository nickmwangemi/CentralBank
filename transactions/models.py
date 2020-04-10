from django.db import models
from datetime import date
from accounts.models import Account
from customers.models import Customer

# Create your models here.


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(Account,on_delete=models.CASCADE)
    amount =  models.IntegerField()
    recipient = models.ForeignKey(Account,related_name='account',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    mobile_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.amount)
    

class Deposit(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return str(self.amount)

class Withdrawal(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)