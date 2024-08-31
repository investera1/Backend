from rest_framework import generics
from .models import Store
from .serializer import StoreSerializer

from core.permisssions import IsOwnerOrReadOnly

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer 

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsOwnerOrReadOnly]
    