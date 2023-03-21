
from node.models import Node
from node.api.serializers import NodeSerializer

def get_routes(graph_id: int, origin: str, destination: str, max_stops=None) -> list:
    """
    It takes a graph_id, an origin and a destination and returns a list of all possible routes from
    origin to destination
    
    :param graph_id: The id of the graph you want to get the routes from
    :type graph_id: int
    :param origin: The origin city
    :type origin: str
    :param destination: The destination city
    :type destination: str
    :param max_stops: The maximum number of stops to be considered in the route
    :return: A list of paths from origin to destination
    """

    # Initializing vars
    nodes = list()
    source_targets_dict = dict()

    nodes = NodeSerializer(Node.objects.filter(graph_id=graph_id), many=True).data
        
    current_sources = [origin]
    while nodes:

        frontier = [node for node in nodes if node['source'] in current_sources]

        for source in current_sources:
            source_targets_dict.setdefault(source, [])

        current_sources = []

        for node in frontier:
            current_sources.append(nodes.pop(nodes.index(node))['target'])
            source_targets_dict[node['source']].append(node['target'])

    paths = []
    to_visit = [origin]
    while to_visit:
        path = to_visit.pop(0)
        city = path[-1]
        if max_stops and len(path) > int(max_stops):
            continue
        for neighbour in source_targets_dict[city]:
            if neighbour not in path:
                if neighbour == destination:
                    paths.append(path + neighbour)
                else:
                    to_visit.append(path + neighbour)
    
    return paths