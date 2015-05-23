# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150406_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='available_hours_during_project',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='in_project',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='working_hours',
            field=models.FloatField(default=40),
            preserve_default=True,
        ),
    ]
