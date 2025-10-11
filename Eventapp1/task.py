from celery import shared_task
from .models import Booking
from .emails import send_booking_email

@shared_task
def send_booking_email_task(booking_id):
    booking = Booking.objects.get(id=booking_id)
    send_booking_email(booking)