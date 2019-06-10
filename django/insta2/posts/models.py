from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.

def post_image_path(instance, filename):
    return f'posts/image/{filename}'
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = ProcessedImageField(
            upload_to=post_image_path,
            processors=[ResizeToFill(600,600)],
            format='JPEG',
            options={'quality':90},
        )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    