from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet

# Router for products
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Home / test
    path('', views.home),
    path('test/', views.test_marketplace),

    # Auth
    path('signup/', views.signup),
    path('login/', views.login),

    # Farmers
    path('farmers/', views.farmers),
    path('farmers/add/', views.add_farmer, name='add_farmer'),


    # Fish
    path('fish/', views.fish),
    path('fish/add/', views.add_fish, name='add_fish'),
    # Orders ✅ (IMPORTANT)

    path('orders/', views.get_orders),
    path('orders/create/', views.create_order),

    # Protected actions
    path('buy-fish/<int:id>/', views.buy_fish),
    path('my-fish/', views.my_fish),
    path('add-fish/', views.add_fish),

    # Router endpoints (products)
    path('', include(router.urls)),

    path('mpesa/stk-push/', views.mpesa_stk_push, name='mpesa_stk_push'),

]