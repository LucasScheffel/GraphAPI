# REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Others
from graph.models import GraphNodeRelation
from graph.api.serializers import GraphNodeRelationSerializer

class GraphNodeRelationViewSet(ModelViewSet):
    """ Graph-Node Relation viewset """

    serializer_class =  GraphNodeRelationSerializer

    def get_queryset(self, id=None, graph_id=None, node_id=None):

        query = GraphNodeRelation.objects

        if id:
            query = query.filter(id=id)

        if graph_id:
            query = query.filter(graph_id=graph_id)

        if node_id:
            query = query.filter(node_id=node_id)

        return query.all()


    def list(self, request, *args, **kwargs):

        result = self.get_queryset(
            id=request.query_params.get('id', None),
            graph_id=request.query_params.get('graph_id', None),
            node_id=request.query_params.get('node_id', None)
        )

        return Response(self.serializer_class(result, many=True).data, status=status.HTTP_200_OK, headers={})