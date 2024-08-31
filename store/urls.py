from django.urls import path
from .views import StoreList, StoreDetail

urlpatterns = [
    path('',StoreList.as_view(), name="store_list"),
    path('<int:pk>/', StoreDetail.as_view(), name="store_detail" ),
]