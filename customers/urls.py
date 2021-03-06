from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('account_status/<int:pk>/',views.account_status,name='account_status'),
    path('money_transfer/<int:pk>/',views.money_transfer,name='money_transfer'),
    path('money_transfer_detail/<int:pk>/',views.money_transfer_detail,name='money_transfer_detail'),
    path('deposit/<int:pk>/',views.deposit,name='deposit'),
    path('deposit_detail/<int:pk>/',views.deposit_detail,name='deposit_detail'),
    path('withdraw/<int:pk>/',views.withdraw,name='withdraw'),
    path('withdrawal_detail/<int:pk>/',views.withdrawal_detail,name='withdrawal_detail'),
    path('edit_details/<int:pk>/',views.edit_details,name='edit_details'),
]

