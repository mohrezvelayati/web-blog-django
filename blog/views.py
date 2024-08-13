from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


from blog.serializers import (PostCreateUpdateSerializer, PostSerializer,
                              PostDetailSerializer, UserSerializer, CommentSerializer,
                              LikesSerializer, BookMarkSerializer
                              )
from blog.models import Post, Comment, Like, BookMark
from .pagination import PostLimitOffsetPagination


# Create your views here.

class UserList(generics.ListCreateAPIView):
    """
    get:
        Returns the list of users

    post:
        Creates a new user. Returns created post data

    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the list of users

    put:
        Updates user data

    patch:
        Updates an existing user

    delete:
        Delete an existing user


    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class PostCreateView(APIView):
    """
    post:
        Creates a new post instance. Returns created post data
    """

    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class PostListView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostLimitOffsetPagination


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a post instance. Searches post using slug field.

    put:
        Updates an existing post. Returns updated post data

    delete:
        Delete an existing post

    """
    permission_classes = [AllowAny]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class CreateCommentView(CreateAPIView):
    """
     post:
         Create a comment. Returns created comment data

     """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CommentListView(ListAPIView):
    """
    get:
        Returns the list of comments on a particular post

    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Comment.objects.filter(post_id=post_id)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    """
     get:
         Returns the details of a comment.

     put:
         Updates an existing comment. Returns updated comment data

     delete:
         Delete an existing comment

     """

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_fields = ["id"]

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['id'])


class LikeView(CreateAPIView):
    """
     post:
         Like a specific post

     """

    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs['pk'])
        saved = Like.objects.filter(user=user, post=post)
        if saved.exists():
            return Response({"error": "You have already liked this post"})
        else:
            bookmark = BookMark(user=user, post=post)
            bookmark.save()
            return Response({"success": "This post successfully liked for you :)"})

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)


class BookMarkView(CreateAPIView):
    """
     post:
         Bookmark a specific post

     """

    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return BookMark.objects.filter(post_id=post_id)

    def post(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs['pk'])
        saved = BookMark.objects.filter(user=user, post=post)
        if saved.exists():
            return Response({"error": "You have already bookmarked this post"})
        else:
            bookmark = BookMark(user=user, post=post)
            bookmark.save()
            return Response({"success": "This post successfully bookmarked for you :)"})
