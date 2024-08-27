from django.db import models
from apps.users.models import User
# from product.models import ProductCategory
# Create your models here.

# from product.models import Product 

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
    store_name = models.CharField(max_length=50)
    store_description = models.TextField()
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='vendor_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name
    
class VendorProfile(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='profile')
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    
#     