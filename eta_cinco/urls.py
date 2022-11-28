from django.urls import path
from eta_cinco import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'eta_cinco'


urlpatterns = [
    path('list/', v.eta_cinco_list, name='eta_cinco_list'),
    path('add/', v.eta_cinco_add, name='eta_cinco_add'),
    path('update/<int:pk>', v.eta_cinco_update, name='eta_cinco_update'),
    path('delete/<int:pk>', v.eta_cinco_delete, name='eta_cinco_delete'),
]
