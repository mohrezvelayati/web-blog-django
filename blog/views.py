from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import PostCreateUpdateSerializer, PostSerializer, PostDetailSerializer, UserSerializer, CommentSerializer, LikesSerializer, BookMarkSerializer, \
    CommentReplySerializer
from blog.models import Post, Comment, Like, BookMark, CommentReply
from .pagination import PostLimitOffsetPagination


# Create your views here.

class UserList(generics.ListCreateAPIView):
    """

        return users list  ///  اطلاعات کاربران را نمایش میدهد

    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """

        return specific user information  ///  اطلاعات یک کاربر خاص را نمایش میدهد

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

        Getting detail of the post and edit + removing it  ///  نمایش جزئیات ادیت و حذف پست

    """
    permission_classes = [AllowAny]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class CommentListView(generics.ListCreateAPIView):
    """

        return comments of a post  ///  نمایش کامنت های پست

    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     user = self.request.user
    #     post = Post.objects.get(pk=self.kwargs['pk'])
    #     return Comment.objects.filter(message=user.is_authenticated, post=post)


class CommentReplyView(ListCreateAPIView):
    """

        Replying to a comment  //  ریپلای کردن یک کامنت

    """
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LikeView(ListCreateAPIView):
    """

        Liking a post  //  لایک پست

    """
    queryset = Like.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        fav = Like.objects.filter(user=user.is_authenticated, post=post)
        if len(fav) > 0:
            return Response({"error": "You have alredy Liked this post"})
        else:
            like = Like(user=user, post=post)
            like.save()
            return Response({"seccess": "You successfully liked this post :)"})


class BookMarkView(CreateAPIView):
    """

        Bookmark a post  //  بوکمارک پست

    """
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    def get(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        saved = BookMark.objects.filter(user=user.is_authenticated, post=post)
        if len(saved) > 0:
            return Response({"error": "You have alredy Bookmarked this post"})
        else:
            like = BookMark(user=user, post=post)
            like.save()
            return Response({"seccess": "This post successfuly bookmarked for you :)"})
