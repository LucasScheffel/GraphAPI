# Generated by Django 3.2.8 on 2022-09-19 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_delete_graphnoderelation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graph',
            options={'ordering': ['id'], 'verbose_name': 'Graph', 'verbose_name_plural': 'Graphs'},
        ),
        migrations.AlterModelTable(
            name='graph',
            table='graph',
        ),
    ]
