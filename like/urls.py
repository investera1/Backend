from django.urls import path
from .views import LikeDetail, LikeList , User_likes

urlpatterns = [
    path('',LikeList.as_view(), name="Like_list"),
    path('<int:pk>/', LikeDetail.as_view(), name="Like_detail" ),
    path('userLikes/', User_likes.as_view(), name="userLikes_detail"),
]