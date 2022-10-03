from django.db import models

class Graph(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        verbose_name = "Graph"
        verbose_name_plural= "Graphs"
        db_table = "graph"
        ordering = ["id"]


    # Magic Methods and Properties
    def __str__(self):
        return self.description

    # Methods
    def update(self, data):
        self.description = data.get('description', self.description)
        
        self.save()
        return self