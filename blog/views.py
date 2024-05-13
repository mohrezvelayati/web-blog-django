from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response 

from blog.serializers import PostSerializer, UserSerializer, CommentSerializer, LikesSerializer
from blog.models import Post, Comment, Like
# Create your views here.

# ####### first Fault #####
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

    # def get(self, request):
    #     queryset = self.get_queryset()[0]
    #     # print(queryset.comments_count())
    #     return HttpResponse(queryset.comments_count())
    
    '''
    def get(self, request):
        try:
            post_id = self.request.GET.get('id')
            if post_id:
                post = Post.objects.get(id=post_id)
                # Create serializer instance with post data
                serializer = self.get_serializer(post)

                #  Modify serializer to include comments_coun
                serializer.data['comments_count'] = post.comments_count()

                # Return the serialized data (including comments_count)
                return Response(serializer.data)
            else:
                # Handle case where no post_id is provided
                return HttpResponseNotFound('Post ID required')
        except Post.DoesNotExist:
            return HttpResponseNotFound('Post not found')
        '''


class PostDetailView(RetrieveUpdateDestroyAPIView):
    '''Getting detail of the post and edit + removing it'''
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    # def get(self, request):
    #     try:
    #         post_id = self.request.GET.get('id')
    #         if post_id:
    #             post = Post.objects.get(id=post_id)
    #             # Create serializer instance with post data
    #             serializer = self.get_serializer(post)

    #             #  Modify serializer to include comments_coun
    #             serializer.data['comments_count'] = post.comments_count()

    #             # Return the serialized data (including comments_count)
    #             return Response(serializer.data)
    #         else:
    #             # Handle case where no post_id is provided
    #             return HttpResponseNotFound('Post ID required')
    #     except Post.DoesNotExist:
    #         return HttpResponseNotFound('Post not found')


class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class LikeView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]