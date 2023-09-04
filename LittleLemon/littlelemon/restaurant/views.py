from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu, Booking
from .serializers import Menuserializer, BookingSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer