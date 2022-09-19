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

    def get_queryset(self, description=None):
        
        query = Graph.objects

        if description:
            query = query.filter(description__startswith=description)

        return query.all()


    def list(self, request, *args, **kwargs):

        result = self.get_queryset(
            description=request.query_params.get('description', None),
        )

        self.pagination_class.page_size = 20
        page = self.paginate_queryset(result)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                # Creating Graph
                serializer = GraphSerializer(data={'description': request.data['description']})
                serializer.is_valid(raise_exception=True)
                serializer.save()

                # Creating Nodes
                graph_nodes = request.data['data']
                for node in graph_nodes:
                    node['graph_id'] = serializer.data['id']
                    node_serializer = NodeSerializer(data=node)
                    node_serializer.is_valid(raise_exception=True)
                    node_serializer.save()

                response_data = dict(serializer.data)
                response_data.setdefault("data", graph_nodes)

                return Response(response_data, status=status.HTTP_201_CREATED, headers={})
        except Exception as e:
            return Response({'errors': API_Error(e)}, status=status.HTTP_400_BAD_REQUEST, headers={})