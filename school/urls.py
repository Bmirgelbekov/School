
from rest_framework import routers
from django.urls import path

from .views import StudentViewSet, ClassesViewSet, SchoolViewSet


router = routers.DefaultRouter()
router.register('students', StudentViewSet, 'students')
router.register('classes', ClassesViewSet, 'classes')
router.register('school', SchoolViewSet, 'school')


urlpatterns = router.urls