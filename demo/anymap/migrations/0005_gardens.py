# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('anymap', '0004_delete_gardens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gardens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=20, choices=[(b'imperial', 'imperial'), (b'japanese', 'japanese'), (b'stone', 'stone'), (b'flower', 'flower'), (b'other', 'other')])),
                ('rating', models.PositiveIntegerField()),
                ('free_entrance', models.BooleanField(default=False)),
                ('last_renewal', models.DateTimeField()),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
