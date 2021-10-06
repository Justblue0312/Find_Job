from api.viewsets import ProjectViewSet, StudentViewSet, JobPostViewSet, ApplicationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
router.register('student', StudentViewSet)
router.register('jobpost', JobPostViewSet)
router.register('application', ApplicationViewSet)
