from django.urls import path, include

from blog import views

urlpatterns = [
     path('post/', views.PostListView.as_view(), name="post-list"),
    #   path('post/<int:pk>/', views.PostListView.as_view()),
]
