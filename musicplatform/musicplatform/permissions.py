from rest_framework.permissions import BasePermission , SAFE_METHODS
from rest_framework import status
from artists.models import Artist
from rest_framework.exceptions import APIException

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsAuthenticatedUserorReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return not request.user.is_anonymous

class IsUserOrReadOnly (BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
       
class NotUser(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "To fulfil this request, you must be an artist."

class IsTheUserArtistOrReadOnly (BasePermission):
    @property
    def message(self):
        return "Error"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            artist = request.user.artist
        except  Artist.DoesNotExist:
             raise NotUser()
        return True