from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets


from blog.serializers import PostSerializer
from blog.models import Post
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


