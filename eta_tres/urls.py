from django.urls import path
from eta_dois import views as v

# No template tag {% url 'app_name: url_name' objeto.pk %}
app_name = 'eta_dois'


urlpatterns = [
    path('list/', v.eta_dois_list, name='eta_dois_list'),
    path('add/', v.eta_dois_add, name='eta_dois_add'),
    path('update/<int:pk>', v.eta_dois_update, name='eta_dois_update'),
    path('delete/<int:pk>', v.eta_dois_delete, name='eta_dois_delete'),
]
