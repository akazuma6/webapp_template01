#機能1Pythonオブジェクト → JSONへ変換（シリアライズ）
#機能2JSON → Pythonオブジェクトへ変換（デシリアライズ）
# posts/serializers.py
from rest_framework import serializers
from .models import Post
# ModelSerializerを継承して、Postモデル用の翻訳機（シリアライザー）を作成
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # ① どのモデルを翻訳の対象にするかを指定
        model = Post
        # ② どのフィールド（項目）を翻訳に含めるかを指定
        fields = ('id', 'title', 'content', 'created_at')