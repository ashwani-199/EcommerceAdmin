from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff.users'),
    path('add/', views.add, name='staff.add'),
    path('edit/<int:id>/', views.edit, name='staff.edit'),
    path('delete/<int:id>/', views.edit, name='staff.delete'),

]
