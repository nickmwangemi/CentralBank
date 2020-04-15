from django.shortcuts import render,redirect
from customers.models import Customer
from django.contrib import messages
# Create your views here.
# def index(request):
#     return render(request,'dashboard/index.html')

def login(request):
    customers = Customer.objects.all()
    
    if request.method == "POST":
        form = request.POST
        mobile_number = form['mobile_number']
        pin = form['pin']
        mobile_numbers = []
        pins = []

        customer = Customer.objects.get(mobile_number=mobile_number)
        if customer is not None:
            return redirect('customers:account_status',customer.pk)
        else:
            messages.info(request, 'Invalid Phone Number or Pin')
        
    return render(request,'dashboard/login.html')

   
    

