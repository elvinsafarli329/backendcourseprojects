from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import myBlogSerializer
from rest_framework import viewsets
from ..models import myBlog

class RaceAPIpage(ListAPIView):
    queryset = myBlog.objects.all()
    serializer_class = myBlogSerializer
    
class myBlogViewSet(viewsets.ModelViewSet):
    queryset = myBlog.objects.all()
    serializer_class = myBlogSerializer

class RaceDetailAPIpage(RetrieveAPIView):
    queryset = myBlog.objects.all()
    serializer_class = myBlogSerializer
    lookup_field = "pk"

class RaceDeleteAPIpage(DestroyAPIView):
    queryset = myBlog.objects.all()
    serializer_class = myBlogSerializer
    lookup_field = "pk"

class RaceUpdateAPIpage(UpdateAPIView):
    queryset = myBlog.objects.all()
    serializer_class = myBlogSerializer
    lookup_field = "pk"
