from rest_framework import serializers


from blog.models import Category, Post, Comment

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'



class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'author', 'content']


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'