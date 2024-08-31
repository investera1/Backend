from django.urls import path
from .views import StoreList, StoreDetail

urlpatterns = [
    path('render/',StoreList.as_view(), name="store_list"),
    path('render/<int:pk>/', StoreDetail.as_view(), name="store_detail" ),
]