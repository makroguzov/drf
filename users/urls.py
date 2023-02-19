from rest_framework import routers

from .views import ReadOnlyProfileViewSet

router = routers.SimpleRouter()
router.register(r'', ReadOnlyProfileViewSet, basename='user')

urlpatterns = []
urlpatterns += router.urls
