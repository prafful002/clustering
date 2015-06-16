# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anymap', '0003_gardens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gardens',
        ),
    ]
