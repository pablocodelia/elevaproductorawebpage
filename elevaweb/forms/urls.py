from django.urls import include, path
from views import *

urlpatterns = [
    path('/', 'formulario1.html', name='formulario1'),
    path('form2/', enviar, name='form2')

]