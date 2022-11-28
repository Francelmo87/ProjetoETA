from django.urls import path
from saida import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'saida'


urlpatterns = [
    path('list/', v.saida_list, name='saida_list'),
    path('add/', v.saida_add, name='saida_add'),
    path('update/<int:pk>', v.saida_update, name='saida_update'),
    path('delete/<int:pk>', v.saida_delete, name='saida_delete'),
 ]
