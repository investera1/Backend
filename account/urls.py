from django.urls import path
from .views import CustomTokenObtainPairView
from .views import RegisterUserView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
]
