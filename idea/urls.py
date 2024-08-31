from django.urls import path
from .views import IdeaList, IdeaDetail

urlpatterns = [
    path('',IdeaList.as_view(), name="Idea_list"),
    path('<int:pk>/', IdeaDetail.as_view(), name="Idea_detail" ),
]