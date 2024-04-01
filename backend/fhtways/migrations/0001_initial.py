# Generated by Django 5.0.3 on 2024-04-01 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.CharField(max_length=255, unique=True)),
                ('coord', models.JSONField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('description', models.TextField()),
                ('end_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edges_ending', to='fhtways.node')),
                ('start_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edges_starting', to='fhtways.node')),
            ],
        ),
    ]
