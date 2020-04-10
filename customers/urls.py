from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('account_status/<int:pk>/',views.account_status,name='account_status'),
    path('money_transfer/<int:pk>/',views.money_transfer,name='money_transfer'),
    path('deposit/<int:pk>/',views.deposit,name='deposit'),
    path('withdraw/<int:pk>/',views.withdraw,name='withdraw'),
    path('edit_details/<int:pk>/',views.edit_details,name='edit_details'),
]

