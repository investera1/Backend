from rest_framework import generics, permissions
from .models import Store
from .serializer import StoreSerializer

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    