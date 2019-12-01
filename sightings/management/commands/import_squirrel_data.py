from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
from django.utils import timezone
from str2bool import str2bool

import csv

class Command(BaseCommand):
    help = 'import squirrel sightings data'
    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self,*args,**kwargs):
        path = kwargs['path']
        with open(path, 'r') as file:
            rows = csv.reader(file)
            header = next(rows)
            for row in rows:
                t = row[5]
                s = Sighting(
                        latitude = row[0],
                        longitude = row[1],
                        unique_squirrel_id = row[2],
                        shift = row[4],
                        date = timezone.datetime(int(t[4:]),int(t[:2]),int(t[2:4])).date(),
                        age = row[7],
                        primary_fur_color = row[8],
                        location = row[12],
                        specific_location = row[14],
                        running = str2bool(row[15]),
                        chasing = str2bool(row[16]),
                        climbing = str2bool(row[17]),
                        eating = str2bool(row[18]),
                        foraging = str2bool(row[19]),
                        other_activities = row[20],
                        kuks = str2bool(row[21]),
                        quaas = str2bool(row[22]),
                        moans = str2bool(row[23]),
                        tail_flags = str2bool(row[24]),
                        tail_twitches = str2bool(row[25]),
                        approaches = str2bool(row[26]),
                        indifferent = str2bool(row[27]),
                        runs_from = str2bool(row[28]),
                        )
                s.save()
            file.close()

        self.stdout.write(self.style.SUCCESS("Successfully upload squirrel data!"))

