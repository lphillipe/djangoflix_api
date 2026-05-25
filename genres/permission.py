from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permissions(self, request, view):
        return True