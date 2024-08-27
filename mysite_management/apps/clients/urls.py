from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientProfileViewSet, ClientAddressViewSet, ClientOrderViewSet

router = DefaultRouter()
router.register(r'client-profiles', ClientProfileViewSet)
router.register(r'client-addresses', ClientAddressViewSet)
router.register(r'client-orders', ClientOrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
