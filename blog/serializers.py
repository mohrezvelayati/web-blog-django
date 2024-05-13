from rest_framework import serializers
from django.contrib.auth.models import User


from blog.models import Category, Post, Comment, Like



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'is_staff']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def get_comments(self, obj):
        queryset = Comment.objects.filter(all).count()
        return queryset



class LikesSerializer(serializers.ModelSerializer):
    like = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='like-detail'
    )


    
    class Meta:
        model = Like
        fields = ['post_id', 'user_id', 'like']