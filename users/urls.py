from rest_framework import routers

from .views import ProjectViewSet
from .views import ReadOnlyProfileViewSet

router = routers.SimpleRouter()
router.register(r'', ReadOnlyProfileViewSet, basename='user')
router.register(r'(?P<user_pk>[^/.]+)/project', ProjectViewSet, basename='project')

urlpatterns = []
urlpatterns += router.urls
