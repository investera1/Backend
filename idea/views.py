from rest_framework import generics, permissions
from .models import Idea
from .serializer import IdeaSerializer

class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
