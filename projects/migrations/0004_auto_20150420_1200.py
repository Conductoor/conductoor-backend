# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150406_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='start',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
