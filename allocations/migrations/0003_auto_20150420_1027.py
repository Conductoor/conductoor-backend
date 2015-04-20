# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0002_auto_20150331_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allocation',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='allocation',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
