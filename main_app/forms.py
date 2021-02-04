from django.forms import ModelForm
from .models import Routine

class RoutineForm(ModelForm):
  class Meta:
    model = Routine
    fields = ['title', 'dawn', 'sunrise', 'morning', 'noon', 'afternoon', 'evening', 'sunset', 'dusk', 'night', 'midnight', 'source']
