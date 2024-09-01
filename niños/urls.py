from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_niños, name='lista_niños'),
    path('crear/', views.crear_niño, name='crear_niño'),
    path('<int:pk>/editar/', views.editar_niño, name='editar_niño'),
    path('<int:pk>/eliminar/', views.eliminar_niño, name='eliminar_niño'),
    path('asistencia/', views.asistencia, name='asistencia'),
    path('registrar-asistencia/', views.registrar_asistencia,
         name='registrar_asistencia'),
    path('avance-academico/', views.avance_academico, name='avance_academico'),
]
