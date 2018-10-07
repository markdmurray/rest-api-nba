from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet, base_name='players')

urlpatterns = [
    #path('', views.PlayerViewSet.as_view()),
    path('players/<str:aname>', views.PlayerViewSet.as_view()),
]
