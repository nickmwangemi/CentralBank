from django.contrib import admin
from .models import Deposit, Withdrawal, MoneyTransfer

# Register your models here.

class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = [ 'sender','amount','recipient','mobile_number']

class DepositAdmin(admin.ModelAdmin):
    list_display = [ 'amount','timestamp','customer']


class WithdrawalAdmin(admin.ModelAdmin):
   list_display = [ 'amount','timestamp']


admin.site.register(Deposit,DepositAdmin)
admin.site.register(Withdrawal,WithdrawalAdmin)
admin.site.register(MoneyTransfer,MoneyTransferAdmin)


