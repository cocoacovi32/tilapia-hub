from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_marketplace, name='test_marketplace'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# backend/market/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('farmers/', views.farmers, name='farmers'),
    path('fish/', views.fish, name='fish'),
]


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def buy_fish(request, id):
    # Temporary placeholder logic
    return Response({"message": f"Buy fish endpoint works for fish id {id}!"})