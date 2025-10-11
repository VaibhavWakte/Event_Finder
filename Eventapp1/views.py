from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category,Booking
from .forms import EventForm ,BookingForm
from .emails import send_booking_email
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings




def home(request):
    categories = Category.objects.all()
    selected = request.GET.get("category")
    events = Event.objects.all()
    if selected:
        events = events.filter(category__name=selected)
    return render(request, "home.html",
                  {"categories": categories, "events": events, "selected": selected})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "event_detail.html", {"event": event})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EventForm()
    return render(request, "add_event.html", {"form": form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)          # fetch the existing event
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)  # go back to detail page
    else:
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form, 'event': event})
        

"""def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if not request.user.is_authenticated:
        return redirect('login')  # redirect if user not logged in

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # don't save yet
            booking.user = request.user        # assign user
            booking.event = event              # assign event
            booking.save()                     # save to DB

            # Send email confirmation
            send_mail(
                subject="Booking Confirmed!",
                message=f"Hi {request.user.username}, your seat for '{event.title}' is successfully booked!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False,
            )

            return redirect('booking_success')  # redirect to success page
    else:
        form = BookingForm()  # GET request

    return render(request, "book_event.html", {"form": form, "event": event})"""

def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if not request.user.is_authenticated:
        return redirect('login')  # redirect if user not logged in

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)   # don't save yet
            booking.user = request.user         # assign logged-in user
            booking.event = event               # assign event
            booking.save()                      # save to DB

            # Send email to the email entered in the form
            booking.send_booking_email(booking)

            return redirect('booking_success')  # redirect to success page
    else:
        form = BookingForm()  # GET request

    return render(request, "book_event.html", {"form": form, "event": event})

def booking_success(request):
    return render(request, 'booking_success.html')
    

