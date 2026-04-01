# tilapia_backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth (login/signup)
    path('auth/', include('auth_app.urls')),

    # Marketplace (fish, farmers)
    path('marketplace/', include('marketplace_app.urls')),

    # Calculator
    path('calculator/', include('calculator_app.urls')),

    # Notifications
    path('notifications/', include('notifications_app.urls')),
]
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('marketplace/', include('marketplace_app.urls')),  # this line connects marketplace_app
]