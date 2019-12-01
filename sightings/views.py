from django.shortcuts import render

from django.http import HttpResponse

from .models import Sighting

def map(request):
    all_sightings = Sighting.objects.all()[:100]
    context = {'all_sightings': all_sightings}
    return render(request, 'sightings/map.html',context)

def all(request):
    all_sightings = Sighting.objects.all()
    context = {'all_sightings': all_sightings}
    return render(request, 'sightings/all.html', context)

def update(request,unique_squirrel_id):
    return HttpResponse("Hey!")

def add(request):
    return HttpResponse("Here to add!")

def delete(request,unique_squirrel_id):
    return HttpResponse("Hi!")

def stats(request):
    return HttpResponse("Here should be stats!")

