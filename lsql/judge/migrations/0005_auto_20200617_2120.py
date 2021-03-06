# Generated by Django 3.0.7 on 2020-06-17 19:20

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_auto_20200617_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='initial_db',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='problem',
            name='position',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
