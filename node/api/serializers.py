from rest_framework.serializers import ModelSerializer
from node.models import Node

class NodeSerializer(ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'graph_id', 'source', 'target', 'distance']
        extra_kwargs = {'id': {'read_only': True}}