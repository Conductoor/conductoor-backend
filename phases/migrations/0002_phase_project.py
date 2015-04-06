# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('phases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='project',
            field=models.ForeignKey(blank=True, null=True, to='projects.Project', related_name='phases'),
            preserve_default=True,
        ),
    ]
