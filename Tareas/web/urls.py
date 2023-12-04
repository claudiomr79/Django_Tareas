from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name= 'index'),
    path('reservas', views.Ver_Reservas, name='reservas'),
    path('crear', views.reservascreateview.as_view(), name='crear')
] 