from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    
# User: Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    # foreignKey 이 모델의 field가 아니라 외부의 user를 가져온다는 의미

# User: Comment = 1:N
# Post: Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# user1 = User.objects.create(name='Kim')
# user2 = User.objects.create(name='Lee')

# post1 = Post.objects.create(title='1글', user=user1) # (title='1글', user_id=1), (title='1글', user_id=user1.id) 가능
# post2 = Post.objects.create(title='2글', user=user1)
# post3 = Post.objects.create(title='3글', user=user2)

# c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
# c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
# c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
# c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
# c5 = Comment.objects.create(content='1글1댓글', user=user1, post=post2)
# c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
# c7 = Comment.objects.create(content='!2글2댓글', user=user2, post=post2)

# 예시
# 1. 1번 사람이 작성한 게시글은?
# ans) user1.post_set.all()
# <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
# 2. 1번 사람이 작성한 게시글의 댓글들을 출력
# for post in user1.post_set.all():
#     for comment in post.comment_set.all():
#             print(comment.content)
"""
1글1댓글
1글2댓글
1글3댓글
1글4댓글
!1글5댓글
1글1댓글
!2글2댓글
"""
# 3. 2번 댓글을 쓴 사람은?
# c2.user
# <User: User object (2)>

# 3.1 2번 댓글을 쓴 사람이 작성한 게시글은?
# c2.user.post_set.all() 
# <QuerySet [<Post: Post object (3)>]>
# User와 Post가 1: N 관계로 맺어져 있기 때문에 post_set.all()로 다 읽어 볼수 있다.


# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# post1.comment_set.first().user.name # post1.comment_set.all()[0].user.name
# 'Kim'
# Post와 Comment가 1: N 관계로 맺어져 있기 때문에 comment_set 쓸수 있다.
"""
 post1.comment_set.first()
<Comment: Comment object (1)> # 괄호안의 (1)은 첫번째 댓글이란 말이다.
"""

# 6. '1글'이 제목인 게시글은?
# Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
# Comment.objects.filter(post__title='1글')
# __ 를 쓰면 field를 접근할 수 있다.
# 방법 2
# post1 = Comment.objects.get(title='1글')
# Comment.objects.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 경우?
# Comment.objects.filter(post__title__contains='1')