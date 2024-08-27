from .views import OrderViewSet, OrderHistoryViewSet, OrderItemViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-history', OrderHistoryViewSet)
router.register(r'order-item', OrderItemViewSet)

urlpatterns=[
    path('', include(router.urls)),
]