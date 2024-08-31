from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import CustomTokenObtainPairView  # Import your custom view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('store',include('store.urls')),
  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Use custom view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
