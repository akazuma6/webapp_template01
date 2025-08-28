from django.db import models

# Create your models here.
class Post(models.Model): #Djangoのモデルとして必要な機能（データベースとの連携など）を受け継ぐ
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
#管理画面などで見やすくするための設定
    def __str__(self):
        return self.title