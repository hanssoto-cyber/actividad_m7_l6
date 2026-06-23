from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
]