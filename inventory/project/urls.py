from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from inventory.user.views import register_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.items.urls')),
    path('api/auth/register/', register_user, name='register_user'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login endpoint
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token endpoint
]
