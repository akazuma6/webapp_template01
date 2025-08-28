# posts/urls.py (新規作成)
#views.pyでPostViewSetを作りましたが、これだけではまだ外部からアクセスできません。どのURLにアクセスすればどの機能が呼び出されるのか、という対応付け（ルーティング）を設定する必要があります
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# ① ルーターを作成
router = DefaultRouter()

# ② URLのプレフィックスとViewSetを登録
router.register(r'posts', PostViewSet)

# ③ 生成されたURLをDjangoに認識させる
urlpatterns = router.urls