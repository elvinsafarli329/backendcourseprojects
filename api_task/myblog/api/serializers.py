from rest_framework import serializers
from ..models import myBlog

class myBlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = myBlog
        fields = ["id","color", "region", "draft", "image"]
