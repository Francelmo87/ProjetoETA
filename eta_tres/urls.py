from django.urls import path
from eta_tres import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'eta_tres'


urlpatterns = [
    path('list/', v.eta_tres_list, name='eta_tres_list'),
    path('add/', v.eta_tres_add, name='eta_tres_add'),
    path('update/<int:pk>', v.eta_tres_update, name='eta_tres_update'),
    path('delete/<int:pk>', v.eta_tres_delete, name='eta_tres_delete'),
]
