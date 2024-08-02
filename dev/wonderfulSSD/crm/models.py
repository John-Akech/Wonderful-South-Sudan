from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    TOUR_CHOICES = [
        ('Natural Wonders', 'Natural Wonders'),
        ('Cultural Tours', 'Cultural Tours'),
        # Add more options as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    tour = models.CharField(max_length=100, choices=TOUR_CHOICES)
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.tour}"
