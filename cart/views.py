from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        # Call the default create method
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Return the created cart object along with a custom response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
