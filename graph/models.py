from django.db import models

class Graph(models.Model):
    class Meta:
        verbose_name = "Graph"
        verbose_name_plural= "Graphs"

class GraphNodeRelation(models.Model):
    graph_id = models.ForeignKey(Graph, null=False, related_name="graphs", on_delete=models.CASCADE)
    node_id = models.ForeignKey('node.Node', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Graph-Node Relation"
        verbose_name_plural = "Graph-Node Relations"
        unique_together = [["graph_id", "node_id"]]