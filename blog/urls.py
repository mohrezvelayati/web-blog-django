from django.urls import path

from blog import views

urlpatterns = [

    # User
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),

    # Post
    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/create', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),

    # Comment
    path("post/<str:slug>/comment/create/", views.CreateCommentView.as_view(), name="comment-create"),
    path('post/<int:pk>/comment/', views.CommentListView.as_view(), name="comment-list"),
    path('post/<int:post_id>/comment/<int:id>/', views.CommentDetailView.as_view(), name="comment-detail"),

    # Like
    path('post/<int:pk>/like/', views.LikeView.as_view(), name='likes'),

    # BookMark
    path('post/<int:pk>/bookmark/', views.BookMarkView.as_view(), name='bookmarks'),
]
