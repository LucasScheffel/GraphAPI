""" core URL Configuration """

#Django
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
# Rest Framework
from rest_framework import routers
# Views and ViewSets
from node.api.viewsets import NodeViewSet
from graph.api.viewsets import GraphNodeRelationViewSet

router = routers.DefaultRouter()
router.register(r'node', NodeViewSet, basename="Node")
router.register(r'graph-node-relation', GraphNodeRelationViewSet, basename="Graph-Node-Relation")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
