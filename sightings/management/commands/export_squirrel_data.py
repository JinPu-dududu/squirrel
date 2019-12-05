from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting

import csv

class Command(BaseCommand):
    help = 'export squirrel sightings data'
    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self,*args,**options):
        path = kwargs['path']
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow([f.name for f in Sighting._meta.get_fields()][1:])
            for i in Sighting.objects.all():
                writer.writerow([
                        i.latitude,
                        i.longitude,
                        i.unique_squirrel_id,
                        i.shift,
                        i.date,
                        i.age,
                        i.primary_fur_color,
                        i.location,
                        i.specific_location,
                        i.running,
                        i.chasing,
                        i.climbing,
                        i.eating,
                        i.foraging,
                        i.other_activities,
                        i.kuks,
                        i.quaas,
                        i.moans,
                        i.tail_flags,
                        i.tail_twitches,
                        i.approaches,
                        i.indifferent,
                        i.runs_from,
                        ])
            file.close()
        self.stdout.write(self.style.SUCCESS("Successfully export squirrel data!"))
