from django.db import models
from django.utils import timezone

from django.utils.translation import gettext as _

class Sighting(models.Model):
    longitude = models.DecimalField(
            max_digits=15,
            decimal_places=13,
            )

    latitude = models.DecimalField(
            max_digits=15,
            decimal_places=13,
            )

    unique_squirrel_id = models.CharField(
            max_length=255,
            )
    
    AM = 'am'
    PM = 'pm'
    SHIFT_CHOICES = (
            (AM, 'am'),
            (PM, 'pm'),
            )
    shift = models.CharField(
            max_length=16,
            choices=SHIFT_CHOICES,
            default=AM,
            )
    
    date = models.DateField(
            default=timezone.now,
            )
    
    JUVENILE = 'juvenile'
    ADULT = 'adult'
    AGE_CHOICES = (
            (JUVENILE, 'juvenile'),
            (ADULT, 'adult'),
            )
    age = models.CharField(
            max_length=16,
            choices=AGE_CHOICES,
            default=JUVENILE,
            )
    
    GRAY = 'gray'
    CINNAMON = 'cinnamon'
    BLACK = 'black'
    FUR_CHOICES = (
            (GRAY, 'gray'),
            (CINNAMON, 'cinnamon'),
            (BLACK, 'black')
            )
    primary_fur_color = models.CharField(
            max_length=16,
            choices=FUR_CHOICES,
            default=GRAY,
            )
    
    ABOVE = 'above ground'
    PLANE = 'ground plane'
    LOCATION_CHOICES = (
            (ABOVE, 'above ground'),
            (PLANE, 'ground plane'),
            )
    location = models.CharField(
            max_length=16,
            choices=LOCATION_CHOICES,
            default=ABOVE,
            )

    specific_location = models.TextField(
            help_text=_('Please specify the location.'),
            )
    
    running = models.BooleanField(
            help_text=_('Squirrel was seen running.'),
            default=False,
            )

    chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing.'),
            default=False,
            )

    climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing.'),
            default=False,
            )

    eating = models.BooleanField(
            help_text=_('Squirrel was seen eating.'),
            default=False,
            )

    foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging.'),
            default=False,
            )

    other_activities = models.TextField(
            help_text=_('Please describe if not listed above.'),
            )

    kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking.'),
            default=False,
            )

    quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing.'),
            default=False,
            )

    moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning.'),
            default=False,
            )

    tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail.'),
            default=False,
            )

    tail_twitches = models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail.'),
            default=False,
            )

    approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human.'),
            default=False,
            )

    indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence.'),
            default=False,
            )

    runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans.'),
            default=False,
            )
    def __str__(self):
        return f"{self.unique_squirrel_id}"

