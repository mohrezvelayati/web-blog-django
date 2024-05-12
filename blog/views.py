from django.shortcuts import render
from rest_framework import generics

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User


from blog.serializers import PostSerializer, UserSerializer, CommentSerializer
from blog.models import Post, Comment
# Create your views here.

# ####### first Fault #######
"""
class PostListView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    lookup_field = 'post-list'


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
"""

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer




class PostListView(ListCreateAPIView):
    '''Getting list of posts and creating new posts'''
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class PostDetailView(RetrieveUpdateDestroyAPIView):
    '''Getting detail of the post and edit + removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]