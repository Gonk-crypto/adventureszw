from django.contrib import admin
from app.models import Adventure, Booking, Event, PriceSchedule
admin.site.register(Adventure)
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(PriceSchedule)
# Register your models here.
