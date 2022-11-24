from django.urls import path
from eta_um import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'eta_um'

urlpatterns = [
    path('add/', v.eta_um_add, name='eta_um_add'),
    path('list/', v.eta_um_list, name='eta_um_list'),
    path('update/<int:pk>', v.eta_um_update, name='eta_um_update'),
    path('delete/<int:pk>', v.eta_um_delete, name='eta_um_delete'),
]
