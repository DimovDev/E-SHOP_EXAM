from rest_framework import permissions


class AdminOrUpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        if request.method in permissions.SAFE_METHODS:
            return True

        is_admin = request.user and \
                   request.user.is_active and \
                   request.user.is_staff

        return (obj.id == request.user.id) or is_admin
