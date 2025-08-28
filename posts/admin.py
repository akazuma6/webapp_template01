# posts/admin.py
from django.contrib import admin
from .models import Post # Postモデルをインポート

# Register your models here.
admin.site.register(Post) # この行を追加