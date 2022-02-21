from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(
        auto_created=True, primary_key=True, unique=True)
    customer_fname = models.CharField(max_length=25)
    customer_lname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    phone_number=models.CharField(max_length=10)


    class Meta:
        db_table = "customer"
