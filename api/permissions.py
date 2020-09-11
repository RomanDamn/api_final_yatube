from rest_framework import permissions
from rest_framework.permissions import BasePermission


class OwnResourcePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user == obj.author
        return True
