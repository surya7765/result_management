from django.urls import path, include
from stapi.views import Home, StudentViewSet, SubMarksViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api-student', StudentViewSet, basename='api-student')
router.register(r'api-student-marks', SubMarksViewSet, basename='api-student-marks')


urlpatterns = [
    path('', Home, name="stapi-home"),
    path('', include(router.urls)),
]
