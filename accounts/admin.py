from django.contrib import admin
from .models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display= ['account_number','balance','account_type','currency']

admin.site.register(Account,AccountAdmin)