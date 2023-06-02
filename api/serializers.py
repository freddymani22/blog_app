from rest_framework import serializers

from blog.models import Post,Comment


class PostSerializer(serializers.ModelSerializer):
    author= serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['title','profile_pic', 'content', 'date_posted', 'author', 'img_post', 'slugs','comments']


    def get_author(self,obj):
        return obj.author.username
    

    def get_profile_pic(self,obj):
        return obj.author.profile.image.url
    

    def get_comments(self,obj):
        qs = obj.comment_set.all()
        serializer = PostCommentSerializer(qs, many=True)
        return serializer.data
    

class PostCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['username','comment_text']

    

    def get_username(self, obj):
       return  obj.user.username

    
