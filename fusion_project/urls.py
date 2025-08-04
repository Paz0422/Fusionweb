from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contacto/', include('contacto.urls')),
    path('nosotros/', include('nosotros.urls')),
    path('productos/', include('productos.urls')),
]
