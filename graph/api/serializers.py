from rest_framework.serializers import ModelSerializer

from node.api.serializers import NodeSerializer
from graph.models import Graph

class GraphSerializer(ModelSerializer):
    class Meta:
        model = Graph
        fields = ['id']