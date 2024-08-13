from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Category, Post, Comment, Like, BookMark


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'is_staff'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'post',
            'message',
            'email',
            'approved',
            'created_date',
            'parent',
        ]

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return None

    def get_comments(self, post):
        return Comment.objects.filter(post=post).count()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, post):
        return Like.objects.filter(post=post).count()

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'content',
            'image',
            'category',
            'likes',
            'bookmark_count'
        ]


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'content',
            'published_date',
            'status',
            'category',
            'comments_count',
            'likes',
            'bookmark_count'
        ]

    def get_likes(self, post):
        return Like.objects.filter(post=post).count()


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'content',
            'image',
            'category',
            'likes',
            'bookmark_count',
            'comments',
            'published_date',
            'status',
        ]

    def get_likes(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_comments(self, obj):
        related_comments = Comment.objects.filter(post=obj)
        try:
            serializer = CommentSerializer(related_comments, many=True)
        except Exception as e:
            print(e)
        return serializer.data


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id',
            'user'
        ]


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = [
            'id',
            'user'
        ]
