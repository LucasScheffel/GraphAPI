# Generated by Django 3.2.8 on 2022-09-13 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_alter_graphnoderelation_graph_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graphnoderelation',
            options={'ordering': ['id'], 'verbose_name': 'Graph-Node Relation', 'verbose_name_plural': 'Graph-Node Relations'},
        ),
    ]
