# Generated by Django 3.2.8 on 2022-09-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0005_auto_20220919_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='description',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
