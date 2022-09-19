from rest_framework.serializers import ModelSerializer

from graph.models import Graph
from node.api.serializers import NodeSerializer

class GraphSerializer(ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    class Meta:
        model = Graph
        fields = ['id', 'description', 'nodes']