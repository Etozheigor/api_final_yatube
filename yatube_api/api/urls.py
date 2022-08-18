from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

v1_router = DefaultRouter()

v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
v1_router.register(r'posts', PostViewSet, basename='post')
v1_router.register(r'groups', GroupViewSet, basename='group')
v1_router.register(r'follows', FollowViewSet, basename='follow')


app_name = 'api'

urlpatterns = [
    path('v1/', include(v1_router.urls)), ]


