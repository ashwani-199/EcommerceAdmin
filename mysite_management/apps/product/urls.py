from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='product.index'),
   path('add/', views.addProduct, name='product.add'),
   path('add-category/', views.addCategory, name='product.add_category'),
   path('edit/<int:id>/', views.edit, name='product.edit'),
   path('delete/<int:id>/', views.delete, name='product.delete'),
   
]