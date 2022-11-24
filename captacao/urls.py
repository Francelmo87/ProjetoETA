from django.urls import path
from captacao import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'captacao'


urlpatterns = [
    path('list/', v.captacao_list, name='captacao_list'),
    path('add/', v.captacao_add, name='captacao_add'),
    path('update/<int:pk>', v.captacao_update, name='captacao_update'),
    path('delete/<int:pk>', v.captacao_delete, name='captacao_delete'),
 ]
