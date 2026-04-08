from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fish, Order

# ================= React Frontend View =================
class FrontendAppView(TemplateView):
    """
    Serves the React frontend app.
    All URLs not handled by Django REST API will render index.html.
    """
    template_name = "index.html"


# ================= Tasks API =================
@api_view(['GET'])
def get_tasks(request):
    """
    Return a list of tasks (example: feeding tasks for fish).
    """
    tasks = [{"id": 1, "task": "Feed fish"}]  # Replace with DB query if you have a Task model
    return Response(tasks)


@api_view(['POST'])
def add_task(request):
    """
    Add a new task (example).
    """
    task = request.data.get("task")
    if not task:
        return Response({"error": "Task is required"}, status=400)
    # Here you can save to DB if you have a Task model
    return Response({"message": f"Task '{task}' added!"})


# ================= Fish API =================
@api_view(['GET'])
def get_fish(request):
    """
    Get all fish from the database.
    Returns: id, name, price_per_kg, quantity
    """
    fish_list = Fish.objects.all().values("id", "name", "price_per_kg", "quantity")
    return Response(list(fish_list))


# ================= Orders API =================
@api_view(['GET'])
def get_orders(request):
    """
    Get all orders.
    Returns: id, total, created_at
    """
    orders = Order.objects.all().values("id", "total", "created_at")
    return Response(list(orders))


@api_view(['POST'])
def create_order(request):
    """
    Create a new order with total amount.
    """
    total = request.data.get("total")
    if total is None:
        return Response({"error": "Total is required"}, status=400)
    order = Order.objects.create(total=total)
    return Response({"message": "Order created", "order_id": order.id})


# ================= Mpesa API (Placeholder) =================
@api_view(['POST'])
def mpesa_stk_push(request):
    """
    Trigger a Mpesa STK push (placeholder for actual implementation).
    """
    # Example: parse amount, phone number etc. from request.data
    return Response({"message": "Mpesa STK push triggered (placeholder)"})


# ================= Optional: Health Check =================
@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint for uptime monitoring.
    """
    return Response({"status": "ok"})