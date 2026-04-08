from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # AUTH
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('auth_app.urls')),

    # TASKS
    path('api/tasks/', views.get_tasks, name='get_tasks'),
    path('api/tasks/add/', views.add_task, name='add_task'),

    # FISH
    path('api/fish/', views.get_fish, name='get_fish'),

    # ORDERS
    path('api/orders/', views.get_orders, name='get_orders'),
    path('api/orders/create/', views.create_order, name='create_order'),

    # MPESA
    path('api/mpesa/stk-push/', views.mpesa_stk_push, name='mpesa_stk_push'),

    # HEALTH CHECK
    path('api/health/', views.health_check, name='health_check'),
]

# REACT FRONTEND CATCH-ALL
urlpatterns += [
    re_path(r'^.*$', views.FrontendAppView.as_view(), name='frontend'),
]