from django.db import models
from django.urls import reverse


class PriceSchedule(models.Model):
    participants = models.PositiveSmallIntegerField()
    adventure = models.ForeignKey('app.Adventure', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return str(self.adventure) + ': ' + str(self.participants)
# Create your models here.
class Adventure(models.Model):
    duration = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    days = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    date = models.DateField()

    def total(self):
        return sum([i.subtotal for i in self.bookingline_set.all()])

    def get_absolute_url(self):
        return reverse("app:booking-detail", kwargs={"pk": self.pk})

class BookingLine(models.Model):
    booking = models.ForeignKey('app.booking', on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    number_of_participants = models.IntegerField()

    @property
    def subtotal(self):
        pricing = PriceSchedule.objects.get(adventure=self.adventure, 
            participants=self.number_of_participants)

        return pricing.price * self.number_of_participants



    

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length=255)
    image = models.ImageField()
    