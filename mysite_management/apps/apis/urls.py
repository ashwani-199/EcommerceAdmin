from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ProductViewSet, ProductCategoryViewSet, ProductImageViewSet, ProductReviewViewSet, ProductVarientViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce Website API",
      default_version='v1',
      description="Online Ecommerce Website",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('v1/products/', ProductViewSet.as_view({'get': 'list'})),
   path('v1/products-category/', ProductCategoryViewSet.as_view({'get': 'list'})),
   
   
]