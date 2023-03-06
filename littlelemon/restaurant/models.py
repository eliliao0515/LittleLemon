from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

validators = [
    MaxValueValidator(5)
]
# Create your models here.
class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True, validators = [
                                                    MaxValueValidator(5)
                                                ])
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField(validators = [
                                                    MaxValueValidator(5)
                                                ])
    
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

class Booking(models.Model):
    id = models.IntegerField(primary_key=True, validators = [
                                                    MaxValueValidator(11)
                                                ])
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(validators = [
                                                    MaxValueValidator(6)
                                                ])
    bookingDate = models.DateTimeField()