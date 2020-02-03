from django.urls import path 
from app import views
from rest_framework.routers import DefaultRouter

event_router = DefaultRouter()
event_router.register(r'^api/event', views.EventAPIView)

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('pricing/', views.Pricing.as_view(), name='pricing'),
    path('terms/', views.Terms.as_view(), name='terms'),
    path('booking-detail/<int:pk>', views.BookingDetail.as_view(), 
        name='booking-detail'),
    path('book-our-adventures/', views.BookAdventure.as_view(), 
        name='book-our-adventures'),
    path('eat/', views.Eat.as_view(), name='eat'),
    path('calendar/month/<int:year>/<int:month>', views.EventsView.as_view(), 
        name='calendar'),
    path('api/events/<int:year>/<int:month>/', views.get_events, 
        name='api-events'),
    path('event-detail/<int:pk>/', views.EventDetail.as_view(), 
        name='event-details'),
    path('play/', views.Play.as_view(), name='play'),
    path('add-booking-line/', views.add_to_booking, name='add-booking-line'),
    path('relax/', views.Relax.as_view(), name='relax'),
    path('adventure/<int:pk>', views.AdventureDetail.as_view(), 
        name='bookings'),
    path('create-booking/', views.BookingCreate.as_view(),
        name='create-booking')
    ,
    path('get-price/<int:adventure>/<int:participants>/', views.get_price,
        name='get-price')
] + event_router.urls
