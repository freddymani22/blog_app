from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentsInline(admin.StackedInline):
    model = Comment


class Postadmin(admin.ModelAdmin):
    inlines = [CommentsInline]
    list_display = ['id', 'title', 'slugs']
    raw_id_fields = ['author']


admin.site.register(Post, Postadmin)






