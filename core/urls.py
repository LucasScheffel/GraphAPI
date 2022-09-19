""" core URL Configuration """

#Django
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
# Rest Framework
from rest_framework import routers
# Views and ViewSets
from node.api.viewsets import NodeViewSet
from graph.api.viewsets import GraphViewSet
from graph.views import *

router = routers.DefaultRouter()
router.register(r'node', NodeViewSet, basename="Node")
router.register(r'graph', GraphViewSet, basename="Graph")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('routes/<int:graph_id>/from/<str:town1>/to/<str:town2>', graph_routes),
    path('distance/<int:graph_id>/from/<str:town1>/to/<str:town2>', graph_min_distance)
]
