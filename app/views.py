from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,DetailView,CreateView
from app.models import Adventure,Booking, BookingLine, Event, PriceSchedule
from app import forms
from django.http import JsonResponse
from app.serializers import EventSerializer
import os
from rest_framework import viewsets
import datetime
import calendar
from django.http import JsonResponse, HttpResponse

class Home(TemplateView):
    template_name = os.path.join('app', 'home.html')

class About(TemplateView):
    template_name = os.path.join('app', 'about.html')

class Pricing(TemplateView):
    template_name = os.path.join('app', 'pricing.html')

class Eat(TemplateView):
    template_name = os.path.join('app', 'eat.html')

class Play(TemplateView):
    template_name = os.path.join('app', 'play.html')

class Relax(TemplateView):
    template_name = os.path.join('app', 'relax.html')

class BookAdventure(TemplateView):
    template_name = os.path.join('app', 'book_adventure.html')

class Events(TemplateView):
    template_name = os.path.join('app', 'home.html')

class Terms(TemplateView):
    template_name = os.path.join('app', 'terms.html')

class AdventureDetail(DetailView):
    model = Adventure
    template_name = os.path.join('app', 'details.html')

class BookingCreate(CreateView):
    template_name = os.path.join('app' , 'booking_create.html')
    form_class = forms.BookingForm


    def form_valid(self, form):
        resp =  super().form_valid(form)

        for line in self.request.session['booking']:
            BookingLine.objects.create(
                booking=self.object,
                adventure=Adventure.objects.get(pk=line['adventure']),
                number_of_participants=line['participants']
            )
        self.request.session['booking'] = []
        return resp


class BookingDetail(DetailView):
    model = Booking
    template_name = os.path.join('app', 'booking_details.html')

class EventDetail(DetailView):
    model = Event
    template_name = os.path.join('app', "event_details.html")


class EventsView(TemplateView):
    template_name = os.path.join('app', 'events.html')

def get_price(request, adventure=None, participants=None):
    pricing = get_object_or_404(PriceSchedule, adventure=adventure, 
        participants=participants)

    return JsonResponse({'price': pricing.price})


class EventAPIView(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class = EventSerializer

def get_events(request, year=None, month=None):
    year= int(year)
    month= int(month)
    first = datetime.date(year, month, 1)
    last = datetime.date(year, month, calendar.monthrange(year, month)[1])
    events = Event.objects.filter(
        date__gte=first,
        date__lte=last
    )

    return JsonResponse([{
        'id': evt.pk,
        'date': evt.date,
        'title': evt.title
    } for evt in events], safe=False)


def add_to_booking(request):
    booking = request.session.get('booking', [])
    booking.append({
        'adventure': request.POST['adventure'],
        'participants': request.POST['participants'],
        'price': request.POST['price'],
        'price_total': float(request.POST['price']) * int(request.POST['participants']),
        'adventure_string': Adventure.objects.get(
            pk=request.POST['adventure']).name
    })
    request.session['booking'] = booking
    request.session['total'] = sum([float(i['price']) * int(i['participants']) for i in booking])
    # print(request.session['booking'])
    return HttpResponse('')