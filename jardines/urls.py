from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_jardines, name='lista_jardines'),
    path('crear/', views.crear_jardin, name='crear_jardin'),
    path('<int:pk>/editar/', views.editar_jardin, name='editar_jardin'),
    path('<int:pk>/eliminar/', views.eliminar_jardin, name='eliminar_jardin'),
]
