from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Farmer, Fish
from .serializers import FarmerSerializer, FishSerializer

# -----------------------------
# FARMERS
# -----------------------------
@api_view(['GET'])
def get_farmers(request):
    farmers = Farmer.objects.all()
    serializer = FarmerSerializer(farmers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_farmer(request):
    serializer = FarmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# -----------------------------
# FISH
# -----------------------------
@api_view(['GET'])
def get_fish(request):
    fish = Fish.objects.all()
    serializer = FishSerializer(fish, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_fish(request):
    serializer = FishSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# -----------------------------
# ORDERS
# -----------------------------
# Example placeholder order data
orders = [
    {"id": 1, "total": 500, "status": "paid"},
]

@api_view(['GET'])
def get_orders(request):
    return Response(orders)

@api_view(['POST'])
def create_order(request):
    new_order = {
        "id": len(orders) + 1,
        "total": request.data['total'],
        "status": "pending"
    }
    orders.append(new_order)
    return Response(new_order)


# -----------------------------
# MPESA STK PUSH (placeholder)
# -----------------------------
@api_view(['POST'])
def mpesa_stk_push(request):
    phone = request.data.get('phone')
    amount = request.data.get('amount')
    # Here you would integrate with Safaricom API
    return Response({"message": f"STK push sent to {phone} for {amount} KES"})