from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['mobile_number','pin']
    # search_fields= ''


admin.site.register(Customer,CustomerAdmin)