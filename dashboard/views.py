from django.shortcuts import render,redirect
from customers.models import Customer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# def index(request):
#     return render(request,'dashboard/index.html')

def login(request):
    if request.method == "POST":
        form = request.POST
        mobile_number = form['mobile_number']
        pin = form['pin']
        
        try:
            customer = Customer.objects.get(mobile_number=mobile_number)

            if (customer.pin == pin):
                return redirect('customers:account_status',customer.pk)
            else:
                messages.info(request, 'Invalid Phone Number or PIN')

        except ObjectDoesNotExist as ex:
            messages.info(request, 'Invalid Phone Number or PIN')
            return render(request,'dashboard/login.html')
        
    return render(request,'dashboard/login.html')

   
    

