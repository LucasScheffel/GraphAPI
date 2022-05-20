
from node.models import Node
from node.api.serializers import NodeSerializer
from graph.models import GraphNodeRelation
from graph.api.serializers import GraphNodeRelationSerializer

def get_routes_from_graph(graph_id: int, origin: str, destination: str, max_stops=None) -> list:
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

    graph_node_relations = GraphNodeRelationSerializer(GraphNodeRelation.objects.filter(graph_id=graph_id).all(), many=True).data

    for relation in graph_node_relations:
        nodes.append(NodeSerializer(Node.objects.get(id=relation['node_id'])).data)

    if not nodes:
        return list()
        
    current_sources = [origin]
    while nodes:

        aux = [node for node in nodes if node['source'] in current_sources]

        for source in current_sources:
            source_targets_dict.setdefault(source, [])

        current_sources = []

        for node in aux:
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