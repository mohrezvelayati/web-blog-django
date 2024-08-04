from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Category, Post, Comment, CommentReply, Like, BookMark


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'is_staff']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'published_date', 'status', 'category', 'comments_count', 'likes',
                  'bookmark_count']

    def get_likes(self, post):
        return Like.objects.filter(post=post).count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def get_comments(self, post):
        return Comment.objects.filter(post=post).count()


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user']


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = ['id', 'user']
