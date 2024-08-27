from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.apis.urls')),
    path('', include('apps.login.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('users/', include('apps.users.urls')),
    path('products/', include('apps.product.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
