from rest_framework.serializers import ModelSerializer

from node.api.serializers import NodeSerializer
from graph.models import Graph, GraphNodeRelation

class GraphSerializer(ModelSerializer):
    class Meta:
        model = Graph
        fields = ['id']

        
class GraphNodeRelationSerializer(ModelSerializer):
    class Meta:
        model = GraphNodeRelation
        fields = ['id', 'graph_id', 'node_id']
        extra_kwargs = {'id': {'read_only': True}}