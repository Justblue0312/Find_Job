from api.viewsets import ProjectViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
