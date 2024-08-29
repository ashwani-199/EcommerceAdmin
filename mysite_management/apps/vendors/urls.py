from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='vendor.index'),
    path('rough/', views.rough, name='vendor.rough'),
    path('add/', views.add, name='vendor.add'),
    # path('edit/<int:id>/', views.edit, name='staff.edit'),
    # path('delete/<int:id>/', views.edit, name='staff.delete'),

]
