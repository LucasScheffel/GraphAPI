""" core URL Configuration """

#Django
from django.contrib import admin
from django.urls import path, include
# Rest Framework
from rest_framework import routers
# Views and ViewSets
from node.api.viewsets import NodeViewSet

router = routers.DefaultRouter()
router.register(r'node', NodeViewSet, basename="Node")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
