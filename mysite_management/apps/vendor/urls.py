from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, VendorProfileViewSet

router = DefaultRouter()
router.register(r'vendor', VendorViewSet)
router.register(r'vendor-profile', VendorProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
