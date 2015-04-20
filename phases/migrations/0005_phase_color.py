# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0004_auto_20150331_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='color',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
