from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('saida/', include('saida.urls')),
    path('eta_cinco/', include('eta_cinco.urls')),
    path('eta_quatro/', include('eta_quatro.urls')),
    path('eta_tres/', include('eta_tres.urls')),
    path('eta_dois/', include('eta_dois.urls')),
    path('eta_um/', include('eta_um.urls')),
    path('captacao/', include('captacao.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
