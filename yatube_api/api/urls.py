from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowListView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', comment_list, name='post-comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', comment_detail,
         name='post-comment-detail'),
    path('auth/', include('djoser.urls')),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    path('follow/', FollowListView.as_view(), name='follow'),
]
