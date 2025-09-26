from django.contrib import admin
from .models import Category, Event,JoinEvent

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "category"]
    list_filter = ["category", "date"]

@admin.register(JoinEvent)
class JoinEventAdmin(admin.ModelAdmin):
    list_display=["name","age","gender","location"]
    