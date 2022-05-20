# Rest Framework
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
# Models and Serializers
from node.models import Node
from graph.models import Graph
from node.api.serializers import NodeSerializer
# Functions
from graph.utils.routes import get_routes_from_graph


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def graph_routes(request, graph_id: int, town1: str, town2: str):
    """
    It takes a graph_id, town1, town2, and max_stops as parameters, and returns a list of all possible
    routes from town1 to town2, with a maximum of max_stops stops
    
    :param request: The request object
    :param graph_id: the id of the graph you want to use
    :type graph_id: int
    :param town1: str, town2: str
    :type town1: str
    :param town2: str
    :type town2: str
    :return: A list of routes from town1 to town2
    """

    if not Graph.objects.filter(id=graph_id).first():
        return Response({}, status=status.HTTP_404_NOT_FOUND, headers={})

    # query param
    max_stops = request.query_params.get('maxStops', None)

    paths = get_routes_from_graph(graph_id, town1.upper(), town2.upper(), max_stops)
    
    routes = [{"route": path, "stops": len(path) - 1} for path in paths]
    return Response({"routes": routes}, status=status.HTTP_200_OK, headers={})


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def graph_min_distance(request, graph_id: int, town1: str, town2: str):
    """
    It takes a graph_id, town1 and town2 as parameters, and returns the minimal distance between town1
    and town2, and the path that leads to that minimal distance
    
    :param request: The request object
    :param graph_id: int
    :type graph_id: int
    :param town1: str, town2: str
    :type town1: str
    :param town2: str, town1: str, graph_id: int
    :type town2: str
    :return: The minimal distance between town1 and town2
    """

    if not Graph.objects.filter(id=graph_id).first():
        return Response({}, status=status.HTTP_404_NOT_FOUND, headers={})
    if town1 == town2:
        return Response({"distance": 0, "path":[town1]}, status=status.HTTP_200_OK, headers={})

    paths = get_routes_from_graph(graph_id, town1.upper(), town2.upper())

    if not paths:
        return Response({"distance": -1, "path": []}, status=status.HTTP_200_OK, headers={})

    distances = dict().fromkeys(paths, 0)
    for path in distances.keys():
        for n in range(len(path) - 1):
            distances[path] += NodeSerializer(Node.objects.filter(source=path[n], target=path[n + 1]).first()).data['distance']

    return Response({"distance": min(distances.values()), "path": list(list(distances.keys())[list(distances.values()).index(min(distances.values()))])}, status=status.HTTP_200_OK, headers={})