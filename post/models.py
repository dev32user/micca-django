from django.db import models
from django.conf import settings


# from account.models import User

class Post(models.Model):
    # 1. 게시글의 id 값
    id = models.AutoField(primary_key=True, null=False, blank=False)
    # 2. 제목
    title = models.CharField(max_length=100)
    # 3. 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 4. 작성자
    # writer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # writer = models.CharField(max_length=20)
    # 5. 본문
    body = models.TextField()
    #
    modify_date = models.DateTimeField(null=True, blank=True)

    # 게시글의 이름을 title로 선언
    def __str__(self):
        return self.title

    # 게시글 요약 정보
    def summary(self):
        return self.body[:10]

# Create your models here.
