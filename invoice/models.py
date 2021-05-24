from django.db import models
from django.contrib.auth.models import  auth


class Organisation(models.Model):

    name = models.CharField(max_length=30, default="Un Known")
    
    def __str__(self):
        return self.name


class Product(models.Model):


    name = models.CharField(max_length = 15, default = "Un Known")
    time = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=10)
    total = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class User(models.Model):
    
    # For now user is temporary
    # Any person can be user without any validation.
    name = models.CharField(max_length= 10)
    def __str__(self):
        return self.name
    
 
class PdfUplaod(models.Model):
    
    pdf = models.FileField(upload_to='pdfs/', default= '')
    
    def __str__(self):
        return str(self.pk)
       
    
    
class Order(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    to_org = models.ForeignKey(
        Organisation, related_name="RECIEVER", on_delete=models.CASCADE)
    from_org = models.ForeignKey(
        Organisation, related_name="SENDER", on_delete=models.CASCADE)
    
    time = models.CharField(max_length=20)
    
    pdf = models.ForeignKey(PdfUplaod, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.user.name
   
'''

    A single order can have multiple product in order.
    One to many relation-ship.

''' 

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "ORDER")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "PRODUCT")
    
    def __str__(self):
        return self.order.user.name + " ----- " + self.product.name
    
