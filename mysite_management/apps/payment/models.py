from django.db import models
from clients.models import ClientProfile  # Import the ClientProfile model
from orders.models import Order
from aadi_app.models import User


class ClientPayment(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    invoice_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.client.user.username} on {self.payment_date}"



class OrderPayment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment #{self.id} by {self.order.client.user.username}"
    


class Payment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} by {self.user.username}"
    

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=200)
    timestamp =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.id} for {self.payment.user.username}"
    

class Invoice(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice of #{self.id} for order #{self.order.id}"