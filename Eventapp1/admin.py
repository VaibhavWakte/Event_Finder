from django.contrib import admin
from .models import Category, Event, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "category"]
    list_filter = ["category", "date"]
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=["user","age","gender","email","phone","seats","event"]
    list_filter = ["user", "gender","event"]