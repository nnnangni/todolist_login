from django.db import models
# 장고의 기본설정
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    # 기본적으로 장고에서 가지고 있는 user모델
    # 유저정보 삭제되면 밑에 게시물도 다 지워지게끔
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title