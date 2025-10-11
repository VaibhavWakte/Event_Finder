from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)        # required column
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='events_banner/',blank=True,null=True)
    location_link = models.URLField(max_length=500,help_text="Paste a full Google Maps URL (e.g. https://maps.google.com/...)") # ⬅️ New: Google Maps link
    
    def __str__(self):
        return self.title   


class Booking(models.Model):
    event = models.ForeignKey('Event',on_delete=models.CASCADE,related_name='bookings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True, blank=True,help_text="If the user is logged in")
    full_name = models.CharField(max_length=100)
    age=models.PositiveIntegerField(help_text="Age in years")
    GENDER_CHOICES=[('M','Male'),('F','Female'),('O','Other'),]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15, help_text="Include country code if needed")
    seats = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.event}"


    def send_booking_email(self, booking):
        to_email = booking.email  # use email entered in form
        if not to_email:
            return False

        subject = f"Booking confirmed — {booking.event.title} (#{booking.id})"
        context = {"booking": booking}
        text_content = render_to_string("booking_confirmation.txt", context)
        html_content = render_to_string("booking_confirmation.html", context)

        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
        return True