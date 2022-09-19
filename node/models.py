from django.db import models

class Node(models.Model):
    graph_id = models.ForeignKey('graph.Graph', null=False, related_name="graphs", on_delete=models.CASCADE)
    source = models.CharField(max_length=1, null=False, blank=False)
    target = models.CharField(max_length=1, null=False, blank=False)
    distance = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.source} to {self.target}"

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"
        db_table = "node"
        unique_together = [["graph_id", "source", "target"]]
        ordering = ['graph_id', 'source']