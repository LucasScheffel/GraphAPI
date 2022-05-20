from django.db import models

class Node(models.Model):
    source = models.CharField(max_length=1, null=False, blank=False)
    target = models.CharField(max_length=1, null=False, blank=False)
    distance = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.source} to {self.target}"

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"
        unique_together = [["source", "target"]]