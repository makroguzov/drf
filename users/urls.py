from rest_framework import routers

from .views import ProjectViewSet
from .views import ReadOnlyProfileViewSet
from .views import TODOViewSet

router = routers.SimpleRouter()
router.register(r'', ReadOnlyProfileViewSet, basename='user')
router.register(r'(?P<user_pk>[^/.]+)/project', ProjectViewSet, basename='project')
router.register(r'(?P<user_pk>[^/.]+)/project/(?P<project_pk>[^/.]+)/todo', TODOViewSet, basename='todo')

urlpatterns = []
urlpatterns += router.urls
