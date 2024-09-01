from reportes import views as reportes_views
from django.urls import path

urlpatterns = [
    path('reportes/', reportes_views.reportes_general, name='reportes_general'),
]