# REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Others
from node.models import Node
from node.api.serializers import NodeSerializer
from graph.models import GraphNodeRelation
from graph.models import Graph
from graph.api.serializers import GraphNodeRelationSerializer, GraphSerializer

class GraphViewSet(ModelViewSet):
    """ Graph Viewset"""
    serializer_class = GraphSerializer
    queryset = Graph.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            # Post the graph id
            serializer = GraphSerializer(data={})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Post node and graph-node-relation
            graph_nodes = request.data['data']
            for node in graph_nodes:
                node_id = None

                existing_node = NodeSerializer(Node.objects.filter(source=node['source'], target=node['target']).first()).data
                if existing_node.get('id'):
                    node_id = existing_node.get('id')
                else:
                    node_serializer = NodeSerializer(data=node)
                    node_serializer.is_valid(raise_exception=True)
                    node_serializer.save()
                    node_id = node_serializer.data['id']

                if node_id:
                    relation_serializer = GraphNodeRelationSerializer(data={'graph_id': serializer.data['id'], 'node_id': node_id})
                    relation_serializer.is_valid(raise_exception=True)
                    relation_serializer.save()

            return Response({'id': serializer.data['id'], 'data': graph_nodes}, status=status.HTTP_201_CREATED, headers={})
        except Exception as e:
            return Response({}, status=status.HTTP_400_BAD_REQUEST, headers={})


    def retrieve(self, request, pk:int):

        if(Graph.objects.filter(id=pk).first()):
            graph_nodes = GraphNodeRelationSerializer(GraphNodeRelation.objects.filter(graph_id=pk).all(), many=True).data
            return Response({'id': pk, 'data': graph_nodes}, status=status.HTTP_200_OK, headers={})
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND, headers={})


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