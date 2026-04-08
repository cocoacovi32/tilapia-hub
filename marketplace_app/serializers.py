from rest_framework import serializers
from .models import Farmer, Fish

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'