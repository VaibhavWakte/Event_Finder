from django import forms
from .models import Event,JoinEvent

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "image","description", "date", "category"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }
class JoinEventForm(forms.ModelForm):
    class Meta:
        model=JoinEvent
        fields=["name","age","gender","location"]
