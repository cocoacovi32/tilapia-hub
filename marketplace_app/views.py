# marketplace_app/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Product, Farmer, Fish
from .serializers import ProductSerializer, FarmerSerializer, FishSerializer


# -----------------------------
# Test Endpoint
# -----------------------------
def test_marketplace(request):
    return HttpResponse("Marketplace app working!")


# -----------------------------
# Product ViewSet (Optional)
# -----------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# -----------------------------
# User Signup
# -----------------------------
@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=400)

    User.objects.create_user(username=username, email=email, password=password)

    return Response({"message": "User registered successfully"})


# -----------------------------
# User Login
# -----------------------------
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({"message": "Login successful"})
    else:
        return Response({"error": "Invalid credentials"}, status=401)


# -----------------------------
# Farmers API
# -----------------------------
@api_view(['GET', 'POST'])
def farmers(request):
    if request.method == 'GET':
        all_farmers = Farmer.objects.all()
        serializer = FarmerSerializer(all_farmers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Farmer added"})
        return Response(serializer.errors, status=400)


# -----------------------------
# Fish API
# -----------------------------
@api_view(['GET', 'POST'])
def fish(request):
    if request.method == 'GET':
        all_fish = Fish.objects.all()
        serializer = FishSerializer(all_fish, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fish added"})
        return Response(serializer.errors, status=400)
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Marketplace API is working ")

    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Welcome to Tilapia Hub Marketplace")

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def buy_fish(request, id):
        return Response({
            "message": f"Fish {id} purchased successfully by {request.user.username}"
        })

    from rest_framework.decorators import api_view
    from rest_framework.response import Response

    @api_view(['POST'])
    def buy_fish(request, id):
        return Response({"message": f"Buy fish endpoint works for fish id {id}!"})

    from rest_framework.decorators import api_view, permission_classes
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.response import Response
    from .models import Fish
    from .serializers import FishSerializer

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def my_fish(request):
        # Filter fish by logged-in user
        fish = Fish.objects.filter(owner=request.user)
        serializer = FishSerializer(fish, many=True)
        return Response(serializer.data)

    from rest_framework.parsers import JSONParser

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def add_fish(request):
        data = request.data
        # Create new fish with logged-in user as owner
        fish = Fish.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            owner=request.user
        )
        serializer = FishSerializer(fish)
        return Response(serializer.data)