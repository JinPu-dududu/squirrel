from django.forms import ModelForm

from .models import Sighting


class SForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
