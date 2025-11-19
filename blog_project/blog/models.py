from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *

class Profile(models.Model):
    author = models.ForeignKey(User, null =True, blank=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null =True, blank=True)
    image = models.ImageField(upload_to='blog',default='blog/default.jpg')
    author = models.ForeignKey(User, null =True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogPost, self).save(*args, **kwargs)    
