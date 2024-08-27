from django.contrib import admin
from .models import ClientProfile, ClientOrder, ClientAddress



# Register your models here.
admin.site.register(ClientProfile)
admin.site.register(ClientAddress)
admin.site.register(ClientOrder)