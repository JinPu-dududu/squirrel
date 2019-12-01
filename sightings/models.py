from django.db import models

from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.DecimalField(
            help_text=_('Latitude'),
            max_digits=15,
            decimal_places=13,
            )

    longitude = models.DecimalField(
            help_text=_('Longitude'),
            max_digits=15,
            decimal_places=13,
            )

    unique_squirrel_id = models.CharField(
            help_text=_('ID'),
            max_length=255,
            )
    
    AM = 'am'
    PM = 'pm'
    SHIFT_CHOICES = (
            (AM, 'am'),
            (PM, 'pm'),
            )
    shift = models.CharField(
            help_text=_('Shift'),
            max_length=16,
            choices=SHIFT_CHOICES,
            )
    
    date = models.DateField(
            help_text=_('Date'),
            )
    
    JUVENILE = 'juvenile'
    ADULT = 'adult'
    AGE_CHOICES = (
            (JUVENILE, 'juvenile'),
            (ADULT, 'adult'),
            )
    age = models.CharField(
            help_text=_('Age'),
            max_length=16,
            choices=AGE_CHOICES,
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
            help_text=_('Primary Fur Color'),
            max_length=16,
            choices=FUR_CHOICES,
            )
    
    ABOVE = 'above ground'
    PLANE = 'ground plane'
    LOCATION_CHOICES = (
            (ABOVE, 'above ground'),
            (PLANE, 'ground plane'),
            )
    location = models.CharField(
            help_text=_('Location'),
            max_length=16,
            choices=LOCATION_CHOICES,
            )

    specific_location = models.TextField(
            help_text=_('Commentart'),
            )
    
    running = models.BooleanField(
            help_text=_('Squirrel was seen running'),
            )

    chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing'),
            )

    climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing'),
            )

    eating = models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            )

    foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging'),
            )

    other_activities = models.TextField(
            help_text=_('Other Activities'),
            )

    kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking'),
            )

    quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing'),
            )

    moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning'),
            )

    tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail'),
            )

    tail_twitches = models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail'),
            )

    approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human'),
                )

    indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence'),
            )

    runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans'),
            )
    def __str__(self):
        return f"<{self.latitude:.3f},{self.longitude:.3f}>: {self.unique_squirrel_id}"

