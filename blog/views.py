from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User


from blog.serializers import PostSerializer, UserSerializer, CommentSerializer, LikesSerializer
from blog.models import Post, Comment, Like
# Create your views here.

# ####### first Fault #####

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer




class PostListView(ListCreateAPIView):
    '''Getting list of posts and creating new posts'''
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        # print(queryset.comments_count())
        return HttpResponse(queryset.comments_count())
    
    # def get(self, request):
    #     try:
    #         post_id = self.request.GET.get('id')
    #         if post_id:
    #             post = Post.objects.get(id=post_id)
    #             return HttpResponse(post.comments_count())
    #     except Post.DoesNotExist:
    #         return HttpResponseNotFound('Post not found')




class PostDetailView(RetrieveUpdateDestroyAPIView):
    '''Getting detail of the post and edit + removing it'''
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class LikeView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]