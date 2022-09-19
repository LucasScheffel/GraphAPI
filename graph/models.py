from django.db import models

class Graph(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.description
        
    class Meta:
        verbose_name = "Graph"
        verbose_name_plural= "Graphs"
        db_table = "graph"
        ordering = ["id"]