from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import models
from .models import Go


def index(request):
    # return HttpResponse("this is the equivalent of the ROOT_route!")
    return render(request, 'ConfluenceAPP/index.html')

def go_process(request):
    errors = Go.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    del_job = Go.objects.get()
    del_job.delete()
    Go.objects.create(mylat=request.POST['ht_lat'], mylong=request.POST['ht_long'])
    return redirect('/landing')

def landing(request):
    context = {
        "pt_lat": Go.objects.get().mylat,
        "pt_long": Go.objects.get().mylong,
    }
    return render(request, 'ConfluenceAPP/landing.html', context)
    # return HttpResponse("this is the equivalent of the landing route!")

# // center: new google.maps.LatLng(52.373922, -3.427734),
# center: new google.maps.LatLng({{pt_lat}}.000000, {{pt_long}}.000000),