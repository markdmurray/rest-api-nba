from django.shortcuts import render
from .models import Players
from rest_framework import generics
from .serializers import PlayerSerializer
# Create your views here.

class PlayerViewSet(generics.ListCreateAPIView):
    queryset = Players.objects.filter(aname='abdelal01')
    serializer_class = PlayerSerializer

class AllPlayerViewSet(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer
