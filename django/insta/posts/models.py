from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def post_image_path(instance, filename ): # instance : 1번 post라면 1번에 해당하는 post를 받는 인자
    return f'posts/image/{filename}'
    # return f'posts/{instance.content}/{instance.content}.jpeg'
    
    
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
                    upload_to=post_image_path, # 저장 위치
                    processors=[ResizeToFill(600, 600)], # 처리할 작업 목록
                    format='JPEG', # 저장 포맷
                    options={'quality':90}, # 옵션
                )
    