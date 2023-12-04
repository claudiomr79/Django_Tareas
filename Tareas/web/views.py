from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.

def Ver_Reservas (request):
   mis_reservas = Reserva.objects.all()

   context = {
        'Lista_reservas':mis_reservas
    }
   return render (request,'web/reservas.html', context)





def index(request):
    return render (request, 'web/index.html', context={})




class reservascreateview (CreateView):
    model = Reserva
    template_name = 'web/crear.html'
    success_url = 'reservas'
    fields ='__all__' 

class reservasdetailview(DetailView):
    model = Reserva
    template_name = 'web/detalle.html'