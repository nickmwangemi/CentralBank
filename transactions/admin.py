from django.contrib import admin
from .models import Deposit, Withdrawal, MoneyTransfer

# Register your models here.

class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = [ 'sender','amount','recipient','mobile_number']

class DepositAdmin(admin.ModelAdmin):
    list_display = [ 'amount','date_of_transaction','customer']


class WithdrawalAdmin(admin.ModelAdmin):
   list_display = [ 'amount','date_of_transaction']


admin.site.register(Deposit,DepositAdmin)
admin.site.register(Withdrawal,WithdrawalAdmin)
admin.site.register(MoneyTransfer,MoneyTransferAdmin)


