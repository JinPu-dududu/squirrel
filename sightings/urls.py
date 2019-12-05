from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
        path('map/', views.map, name='SightingMap'),
        path('sightings/', views.all, name='ShowAllLinks'),
        path('sightings/stats/', views.stats, name='DisplayStats'),
        path('sightings/<unique_squirrel_id>/', views.update, name='Update'),
        path('sightings/add/', views.add, name='Add'),
        ]
