# Generated by Django 3.2.8 on 2022-09-13 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_alter_graphnoderelation_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GraphNodeRelation',
        ),
    ]
