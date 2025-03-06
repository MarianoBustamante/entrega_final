from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cuentas.views import acerca_de_mi



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('', include('cuentas.urls')),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
    # path('', views.inicio, name='inicio'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

