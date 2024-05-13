from django.urls import path, include

from blog import views

urlpatterns = [

    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),


    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),

    path('comment/', views.CommentListView.as_view(), name="comment-list")
]
