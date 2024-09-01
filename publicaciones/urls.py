from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('<int:pk>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('<int:pk>/eliminar/', views.eliminar_publicacion,
         name='eliminar_publicacion'),
]
