# Generated by Django 3.2.8 on 2022-09-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0004_alter_node_table'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='node',
            index=models.Index(fields=['graph_id'], name='graph_id_idx'),
        ),
    ]