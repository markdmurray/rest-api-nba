from django.shortcuts import render
from .models import Players
from rest_framework import generics
from .serializers import PlayerSerializer
# Create your views here.

class PlayerViewSet(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        name = self.kwargs['aname']
        return Players.objects.filter(aname=name)

    #queryset = Players.objects.filter(aname=name)
    

class AllPlayerViewSet(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer
