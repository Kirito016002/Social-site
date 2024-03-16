from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path('user-relation/', views.UserRelationAPIView.as_view()),
    path('chat/', views.UserAPIView.as_view()),
    path('massage/', views.UserAPIView.as_view()),
    path('following/<int:pk>/', views.following),
    path('follower/<int:pk>/', views.follower),
    path('posts/', views.PostAPIView.as_view(), name='post-api'),
    path('comments/', views.CommentAPIView.as_view(), name='comment-api'),
    path('likes/', views.LikeAPIView.as_view(), name='like-api'),
]