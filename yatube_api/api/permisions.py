from rest_framework import permissions
from posts.models import Follow


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Дает возможно изменять или удалять только тот контент,
    автором которого является пользователь."""

    message = 'Изменение чужого контента запрещено'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class DontFollowYourSelf(permissions.BasePermission):
    """Не дает пользователю подписаться на самого себя."""

    message = 'Невозможно подписаться на самого себя'

    def has_permission(self, request, view):
        return (
             request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        
        return obj.following != request.user

class IsFollow(permissions.BasePermission):
    """Не дает пользователю подписаться на пользователя,
    если он уже на него подписан."""

    message = 'Невозможно подписаться, так как вы уже подписаны'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        
        return not Follow.objects.filter(user=request.user, following=obj.following).exists()