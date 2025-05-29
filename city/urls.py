from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllCityViewSet, ComputerRoomNameViewSet, AllHostViewSet

# 使用 DRF 的自动路由
router = DefaultRouter()
router.register(r'cities', AllCityViewSet)
router.register(r'computerroom', ComputerRoomNameViewSet)
router.register(r'hosts', AllHostViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 引入所有视图集的 URL
]
# author xiaogang
