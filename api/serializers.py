from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author= serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['title','profile_pic', 'content', 'date_posted', 'author', 'img_post', 'slugs']


    def get_author(self,obj):
        return obj.author.username
    

    def get_profile_pic(self,obj):
        return obj.author.profile.image.url
    

