# backend/market/serializers.py

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
    # marketplace_app/serializers.py


from rest_framework import serializers
from .models import Fish  # assuming product = fish


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'
