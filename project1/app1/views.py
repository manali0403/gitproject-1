from django.shortcuts import render
from  .serializers import  BlogSerializer
from  .models import Blog
from  rest_framework import  viewsets

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
