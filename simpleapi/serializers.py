from rest_framework import serializers

from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Posts
        #fields = '__all__'
        fields=['title','content','image']