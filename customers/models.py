from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    

    
    class Meta:
        db_table = 'tbl_Customers'

    def __str__(self):
        return self.mobile_number
