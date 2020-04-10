from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.login,name='login'),
    # path('login/',views.index, name='index'),
    
    
]