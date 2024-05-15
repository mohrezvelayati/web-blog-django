from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response 




from blog.serializers import PostSerializer, UserSerializer, CommentSerializer, LikesSerializer, BookMarkSerializer
from blog.models import Post, Comment, Like, BookMark



# Create your views here.

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
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Comment.objects.filter(message=user.is_authenticated, post=post)


class LikeView(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]
            
    def get(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        fav = Like.objects.filter(user=user.is_authenticated, post=post)
        if len(fav) > 0:
            return Response({"error" : "You have alredy Liked this post"})
        else:
            like = Like(user=user, post=post)
            like.save()
            return Response({"seccess" : "You successfully liked this post :)"})




class BookMarkView(ListCreateAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        saved = BookMark.objects.filter(user=user.is_authenticated, post=post)
        if len(saved) > 0:
            return Response({"error" : "You have alredy Bookmarked this post"})
        else:
            like = BookMark(user=user, post=post)
            like.save()
            return Response({"seccess" : "This post successfuly bookmarked for you :)"})