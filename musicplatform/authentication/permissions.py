from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous

