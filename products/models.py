import email
from django.db import models

# Create your models here.

class Products(models.Model):

    product_id=models.AutoField(auto_created=True,primary_key=True)

    product_name=models.CharField(max_length=200)

    product_price=models.CharField(max_length=100)
    product_type=models.CharField(max_length=100,blank=True)

    product_image=models.FileField(upload_to="product_images")


    class Meta:

        db_table="products" 

class Cartproducts(models.Model):

    booking_id=models.AutoField(auto_created=True,primary_key=True)

    pproduct=models.ForeignKey(Products,on_delete=models.CASCADE)

    name=models.CharField(max_length=100)

    email=models.CharField(max_length=100)

    address=models.CharField(max_length=100)

    phonenumber=models.CharField(max_length=50)


    class Meta:

        db_table="booking"


class Seeorder(models.Model):

    product_id=models.AutoField(auto_created=True,primary_key=True)

    product_name=models.CharField(max_length=200)

    product_price=models.CharField(max_length=100)
    product_type=models.CharField(max_length=100,blank=True)

    product_image=models.FileField(upload_to="product_images")


    class Meta:

        db_table="seeorder" 
