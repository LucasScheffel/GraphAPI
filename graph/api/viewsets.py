# REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db import transaction
# Others
from core.utils.errors import API_Error
from node.models import Node
from node.api.serializers import NodeSerializer
from graph.models import Graph
from graph.api.serializers import GraphSerializer

class GraphViewSet(ModelViewSet):
    """ Graph Viewset"""
    serializer_class = GraphSerializer
    queryset = Graph.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                # Post the graph id
                serializer = GraphSerializer(data={})
                serializer.is_valid(raise_exception=True)
                serializer.save()

                # Post node and graph-node-relation
                graph_nodes = request.data['data']
                for node in graph_nodes:
                    # Node
                    node['graph_id'] = serializer.data['id']
                    node_serializer = NodeSerializer(data=node)
                    node_serializer.is_valid(raise_exception=True)
                    node_serializer.save()

                return Response({'id': serializer.data['id'], 'data': graph_nodes}, status=status.HTTP_201_CREATED, headers={})
        except Exception as e:
            return Response({'errors': API_Error(e)}, status=status.HTTP_400_BAD_REQUEST, headers={})


    def retrieve(self, request, pk:int):

        if(Graph.objects.filter(id=pk).first()):
            graph_nodes = NodeSerializer(Node.objects.filter(id__in=self.get_object().graphs.all().only("id")), many=True).data
            return Response({'id': pk, 'nodes': graph_nodes}, status=status.HTTP_200_OK, headers={})
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND, headers={})