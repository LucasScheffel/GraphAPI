from rest_framework.serializers import ModelSerializer

from node.api.serializers import NodeSerializer
from graph.models import Graph, GraphNodeRelation

class GraphNodeRelationSerializer(ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    class Meta:
        model = GraphNodeRelation
        fields = ['id', 'graph_id', 'node_id']
        extra_kwargs = {'id': {'read_only': True}}


class GraphSerializer(ModelSerializer):
    nodes = GraphNodeRelationSerializer(many=True, read_only=True)
    class Meta:
        model = Graph
        fields = ['id', 'nodes']