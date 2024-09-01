from rest_framework import generics, permissions 
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializer import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class User_likes(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter the likes for the authenticated user
        return Like.objects.filter(user=self.request.user)
