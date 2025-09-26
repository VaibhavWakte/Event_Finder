from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)        # required column
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(
        upload_to='events_banner/',blank=True,null=True
    )
    
    def __str__(self):
        return self.title
class JoinEvent(models.Model):
    name=models.CharField(max_length=100,help_text="Enter a full name")
    Gender_Choices=[('M','Male'),('F','Female'),('O','Other'),]
    age=models.PositiveIntegerField(help_text="Age in years")
    gender=models.CharField(max_length=1,choices=Gender_Choices,help_text="Select gender")
    location=models.CharField(max_length=100,help_text="City,State or detailes location")


