from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission


class OwnerOrReadOnly(BasePermission):
    message = "Unrestricted access!"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        elif obj.author != request.user and request:
            raise PermissionDenied(detail=self.message)
        
        return True


class IsSupport(BasePermission):
    message = "Non support user access denied!"

    def has_permission(self, request, view):
        
        if request.method in ("PUT", "PATCH") and request.user.is_superuser:
            return True
        return False
