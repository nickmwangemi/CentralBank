from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from customers.models import Customer


# Create your models here.
class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ("SAVINGS",'Savings'),
        ("CURRENT",'Current'),
    ]
    CURRENCY_CHOICE = [
        ("KENYA SHILLINGS","Kenya Shillings"),
        ("US DOLLAR","US Dollars")
    ]
    account_number = models.PositiveIntegerField(
        # unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ],
        default=10000000
    )
    balance = models.FloatField(
        default=0,
    )
    account_type = models.CharField(max_length=100,choices=ACCOUNT_TYPE_CHOICES,default='SAVINGS')
    currency = models.CharField(max_length=15,choices=CURRENCY_CHOICE,default='KENYA SHILLINGS')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    class Meta:
        db_table = 'tbl_Accounts'

    def __str__(self):
        return str(self.account_number)
