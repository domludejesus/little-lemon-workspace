from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer