from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category,Booking
from .forms import EventForm ,BookingForm

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
def join_event(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=BookingForm()
    return render(request,"joinevent.html",{"form":form})

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
