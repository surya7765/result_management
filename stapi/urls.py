from django.urls import path, include
from stapi.views import Home, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api-student', StudentViewSet, basename='api-student')


urlpatterns = [
    path('', Home, name="stapi-home"),
    path('', include(router.urls)),
]
