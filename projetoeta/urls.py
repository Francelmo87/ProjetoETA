from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('captacao/', include('captacao.urls')),
    path('eta_um/', include('eta_um.urls')),
    path('eta_dois/', include('eta_dois.urls')),
    path('admin/', admin.site.urls),
]
