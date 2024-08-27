from django.contrib import admin
from .models import Product, ProductCategory, ProductImage,ProductReview, ProductVariant
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ProductVariant)