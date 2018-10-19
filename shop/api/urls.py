from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter



from .users.views import UserModelViewSet, LoginViewSet

router = DefaultRouter()
# users
router.register('users', UserModelViewSet)
router.register('login', LoginViewSet, base_name='login')

urlpatterns = [

    url(r'', include(router.urls)),
]
