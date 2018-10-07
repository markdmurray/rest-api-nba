from django.shortcuts import render
from .models import Players
from rest_framework import generics
from .serializers import PlayerSerializer
# Create your views here.

aname = 'abdelal01'

class PlayerViewSet(generics.ListCreateAPIView):
    queryset = Players.objects.filter(aname='abdelal01')
    serializer_class = PlayerSerializer
