# REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Others
from node.api.serializers import NodeSerializer
from node.models import Node

class NodeViewSet(ModelViewSet):
    """ Node viewset """

    serializer_class =  NodeSerializer

    def get_queryset(self, graph_id=None, source=None, target=None):

        query = Node.objects

        if graph_id:
            query = query.filter(graph_id=graph_id)

        if source:
            query = query.filter(source=source)

        if target:
            query = query.filter(target=target)

        return query.all()


    def list(self, request, *args, **kwargs):

        result = self.get_queryset(
            graph_id=request.query_params.get('graph_id', None),
            source=request.query_params.get('source', None),
            target=request.query_params.get('target', None),
        )

        self.pagination_class.page_size = 20
        page = self.paginate_queryset(result)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)
