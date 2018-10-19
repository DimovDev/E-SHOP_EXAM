import users
from django.contrib.auth.views import UserModel
from rest_framework import filters, viewsets, models
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
# POST metoda = uključuje serializers
from . import serializers
from rest_framework import status

# Django viewset
from rest_framework import viewsets


from . import permissions

from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated



from . import serializers, permissions


# LOGIN VIEWSET
class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)


# USER MODEL VIEWSET
class UserModelViewSet(viewsets.ModelViewSet):
    """CRUD on UserModels."""

    serializer_class = serializers.UserModelSerializer
    queryset = UserModel.objects.all()

    # Authentication and Permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AdminOrUpdateOwnProfile,)
    # Add filter functionality
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)  # 'email',  # email not included for privacy reasons
