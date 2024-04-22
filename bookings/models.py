from django.db import models
from django.core.validators import RegexValidator
from tours.models import Tour


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    ]

    phone_regex = RegexValidator(
        regex=r'^\+996-\d{3}-\d{6}$',
        message="Phone number must be entered in the format: '+996-XXX-XXXXXX'."
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    number_of_people = models.PositiveIntegerField()
    additional_comments = models.TextField(blank=True, null=True)
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking by {self.full_name} for {self.tour.name}"
