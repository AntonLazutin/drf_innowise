from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class OwnerPermission(BasePermission):
    message = "Unrestricted access!"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        elif obj.author != request.user:
            raise PermissionDenied(detail=self.message)
        
        return True
        

class SupportPermission(BasePermission):
    message = "Non support user access detected!"

    def has_permission(self, request, view):
        return super().has_permission(request, view)
    

    