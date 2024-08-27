from django.contrib import admin
from . models import Order, OrderHistory, OrderStatus, OrderItem
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderHistory)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)