from django.db import models

class Graph(models.Model):
    class Meta:
        verbose_name = "Graph"
        verbose_name_plural= "Graphs"
        db_table = "graph"
        ordering = ["id"]