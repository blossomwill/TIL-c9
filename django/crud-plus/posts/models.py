from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 길이제한을 꼭 넣어줘야 한다.
    content = models.TextField() # 길이제한이 없다
    def __str__(self):
        return self.title
    
# Post와 Comment가 1:N 관계라면 N쪽에 Post에 대한 정보가 작성된다.
# 그래야 Comment가 누구의 게시글인지 알 수 있다.
# Post : Comment = 1 : N
 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post가 삭제가 되면 어떻게 할건가? 밑에 있는것도 다 삭제하겠다.
    content = models.TextField()

    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL 설정.
    
    
    
    
# 1. Create
# post = Post(title='Hello', content='world!')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all()
# 2.2 Get one
# post = Post.objects.get(pk=1)
# 2.3 filter (WHERE)
# Post.objects.filter(title='Hello').all()
# Post.objects.filter(title='Hello').first()
# 2.4 LIKE
# posts = Post.objects.filter(title__contains='He').all()
# 2.5 order_by (정렬)
# posts = Post.objects.order_by('title').all()
# posts = Post.objects.order_by('-title').all()
# 2.6 limit & offset
# [offset:offset+limit]
# posts = Post.objectcs.all()[1:2]  offset=1, offset+limit=2

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()