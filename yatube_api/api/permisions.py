from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Дает возможность изменять или удалять только тот контент,
    автором которого является пользователь."""

    message = 'Изменение чужого контента запрещено'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
