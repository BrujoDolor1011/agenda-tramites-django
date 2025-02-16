from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tramites, name='lista_tramites'),
    path('nuevo/', views.crear_tramite, name='crear_tramite'),
    path('editar/<int:pk>/', views.editar_tramite, name='editar_tramite'),
    path('eliminar/<int:pk>/', views.eliminar_tramite, name='eliminar_tramite'),
]



