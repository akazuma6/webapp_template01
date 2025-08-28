from django.shortcuts import render
#このコードは、ブログ投稿（Post）に関するAPIのエンドポイント（URLの窓口）一式を自動的に作成するものです。
# Create your views here.
# posts/views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

#Django Rest Framework (DRF) の ViewSet、特に ModelViewSet は、決まりきったAPIのロジック（データベースからデータを取ってきたり、保存したりする処理）をまるごと提供してくれる、非常に便利なクラスです
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer