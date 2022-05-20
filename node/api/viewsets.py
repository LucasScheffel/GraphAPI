# REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Others
from node.api.serializers import NodeSerializer
from node.models import Node

class NodeViewSet(ModelViewSet):
    """ Node viewset """

    serializer_class =  NodeSerializer

    def get_queryset(self, id=None, source=None, target=None, distance=None):

        query = Node.objects

        if id:
            query = query.filter(id=id)

        if source:
            query = query.filter(source=source)

        if target:
            query = query.filter(target=target)

        if distance:
            query = query.filter(distance=distance)

        return query.all()


    def list(self, request, *args, **kwargs):

        result = self.get_queryset(
            id=request.query_params.get('id', None),
            source=request.query_params.get('source', None),
            target=request.query_params.get('target', None),
            distance=request.query_params.get('distance', None)
        )

        return Response(self.serializer_class(result, many=True).data)
