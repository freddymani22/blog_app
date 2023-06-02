from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from django.conf import settings
from PIL import Image
from  django.db.models import Q


User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
    def search(self, query):
        lookup = Q(title__icontains = query)|Q(content__icontains = query)
        return self.filter(lookup)

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using =self._db)

    def search(self, query):
        return self.get_queryset().search(query)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    slugs = models.SlugField(blank=True, null =True, unique=True)
    date_posted = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    img_post = models.ImageField(upload_to='post_images/', null=True, blank=True)
    objects = PostManager()

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'slugs': self.slugs})
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img_post:

            img= Image.open(self.img_post.path)

        
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.img_post.path)

    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text
    


def pre_save_slugs(instance,*args, **kwargs):
    if instance.slugs is None:
        slug = slugify(instance.title)
        instance.slugs = f'{slug}-{instance.id}'

pre_save.connect(pre_save_slugs, sender=Post)



def post_save_slugs(instance, created, *args, **kwargs):
    if created:
            slug = slugify(instance.title)
            instance.slugs = f'{slug}-{instance.id}'
            instance.save()

post_save.connect(post_save_slugs, sender=Post)