from rest_framework import generics
from blog_zona.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postObjects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    pass