from api.models import Players
from rest_framework import serializers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('__all__')