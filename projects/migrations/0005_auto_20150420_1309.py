# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150420_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='end',
            new_name='time_end',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='start',
            new_name='time_start',
        ),
    ]
