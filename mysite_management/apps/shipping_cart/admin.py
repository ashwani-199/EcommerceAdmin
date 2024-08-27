from django.contrib import admin
from .models import ShippingAddress, ShippingCart, Cart, CartItem
# Register your models here.


admin.site.register(ShippingAddress)
admin.site.register(ShippingCart)
admin.site.register(Cart)
admin.site.register(CartItem)