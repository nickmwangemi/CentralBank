from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','id_number','mobile_number','pin']
    search_fields= ['first_name','last_name','id_number','mobile_number']


admin.site.register(Customer,CustomerAdmin)