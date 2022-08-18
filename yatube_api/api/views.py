from posts.models import Group, Post, Comment, Follow
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


#from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    #permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)

    def get_queryset(self):
        commented_post = Post.objects.get(id=self.kwargs.get('post_id'))
        new_queryset = commented_post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        commented_post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=commented_post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    #permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)

    def get_queryset(self):
        new_queryset = self.request.user.following.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, following=self.kwargs.get('id'))  