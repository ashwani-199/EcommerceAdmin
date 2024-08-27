from django.db import models
from clients.models import ClientProfile
from product.models import Product
# Create your models here.


class Order(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=3)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Total amount#{self.total_amount} for order #{self.id}"

class OrderItem(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=100, decimal_places=3)
    price = models.DecimalField(max_digits=100, decimal_places=3)
    total_price = models.DecimalField(max_digits=100, decimal_places=3)

    def __str__(self):
        return f"Total amount#{self.total_price} for order #{self.id}"

class OrderHistory(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    changed_at = models.CharField(max_length=100)

    def __str__(self):
        return self.status
    

class OrderStatus(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status