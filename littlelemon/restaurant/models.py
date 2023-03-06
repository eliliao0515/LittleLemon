from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

validators = [
    MaxValueValidator(5)
]
# Create your models here.
class MenuItem(models.Model):
    Id = models.IntegerField(primary_key=True, validators = [
                                                    MaxValueValidator(5)
                                                ])
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField(validators = [
                                                    MaxValueValidator(5)
                                                ])

class Booking(models.Model):
    Id = models.IntegerField(primary_key=True, validators = [
                                                    MaxValueValidator(11)
                                                ])
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField(validators = [
                                                    MaxValueValidator(6)
                                                ])
    BookingDate = models.DateTimeField()