from django.conf import settings
from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    """Ограничение доступа редактирования или удаления."""
    message = settings.IS_AUTHOR_OR_ADMIN_ERROR_MESSAGE

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff
            or request.user == obj.author
        )
