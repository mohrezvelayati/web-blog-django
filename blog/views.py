from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse


from blog.serializers import PostSerializer
from blog.models import Post
# Create your views here.

class PostListView(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [AllowAny]


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        # return Response(serializer.data)
        return JsonResponse({'foo':'bar'})