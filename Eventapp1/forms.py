from django import forms
from .models import Event,Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "image", "description", "date", "time", "category", "location_link"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'age', 'gender', 'email', 'phone', 'seats']