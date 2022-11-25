from django.urls import path
from eta_quatro import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'eta_quatro'


urlpatterns = [
    path('list/', v.eta_quatro_list, name='eta_quatro_list'),
    path('add/', v.eta_quatro_add, name='eta_quatro_add'),
    path('update/<int:pk>', v.eta_quatro_update, name='eta_quatro_update'),
    path('delete/<int:pk>', v.eta_quatro_delete, name='eta_quatro_delete'),
]
