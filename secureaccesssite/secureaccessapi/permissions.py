from rest_framework import permissions


class IsPasswordCorrect(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.check_password(request.data.get('password'))
