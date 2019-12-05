from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Count
from .models import Sighting

def map(request):
    sightings = Sighting.objects.all()[:100]
    context = {'sightings': sightings}
    return render(request, 'sightings/map.html',context)

def all(request):
    all_sightings = Sighting.objects.all()
    context = {'all_sightings': all_sightings}
    return render(request, 'sightings/all.html', context)

def update(request,unique_squirrel_id):
    return HttpResponse("Hello!")

def add(request):
    return HttpResponse("Here to add!")

def stats(request):
    running1 = Sighting.objects.filter(running=True).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    running0 = Sighting.objects.filter(running=False).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    chasing1 = Sighting.objects.filter(chasing=True).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    chasing0 = Sighting.objects.filter(chasing=False).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    climbing1 = Sighting.objects.filter(climbing=True).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    climbing0 = Sighting.objects.filter(climbing=False).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    eating1 = Sighting.objects.filter(eating=True).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    eating0 = Sighting.objects.filter(eating=False).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    foraging1 = Sighting.objects.filter(foraging=True).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    foraging0 = Sighting.objects.filter(foraging=False).aggregate(Count('unique_squirrel_id'))['unique_squirrel_id__count']
    context = {
            'running1': running1,
            'running0': running0,
            'chasing1': chasing1,
            'chasing0': chasing0,
            'climbing1': climbing1,
            'climbing0': climbing0,
            'eating1': eating1,
            'eating0': eating0,
            'foraging1': foraging1,
            'foraging0': foraging0
            }
    return render(request, 'sightings/stats.html', context)

