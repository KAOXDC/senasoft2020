from django.urls import path
from .views import *

urlpatterns = [
    path('informacion', informacion_vista, name='informacion'),
    path('contacto', contacto_vista, name='contacto'),
    path('', principal_vista, name='principal'),
    path('lista_productos', lista_productos_vista, name='lista_productos'),

]
