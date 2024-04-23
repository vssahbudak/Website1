from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Event
# Create your views here.

def index(request):
    event = Event.objects.all()
    context ={
        'event' : event
    }

    return render (request,'Events/list.html', context)

def detail(request, event_id): #event_id yi urls.py de <int : event_id> olarak belirttik ordan aldık
    
    ### from django.http import Http404 un kullandıgı versiyon
    
    # try:
    #     event = Event.objects.get(pk = event_id)
    # except Event.DoesNotExist:
    #     raise Http404('Kayıt Yok')  

    ### from django.shortcuts import get_object_or_404 un kullandıgı versiyon

    event = get_object_or_404(Event, pk = event_id)

    context = {
        'event': event
    }

    return render (request,'Events/detail.html',context)

def search(request):
    return render (request,'Events/search.html')
