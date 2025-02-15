from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('products.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
