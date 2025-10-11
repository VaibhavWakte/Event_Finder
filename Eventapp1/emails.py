from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_booking_email(booking):
    to_email = booking.user.email if booking.user else booking.guest_email
    if not to_email:
        return False

    subject = f"Booking confirmed — {booking.event.title}"
    context = {"booking": booking}
    text_content = render_to_string("emails/booking_confirmation.txt", context)
    html_content = render_to_string("emails/booking_confirmation.html", context)

    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)
    return True