# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20150331_1402'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='knows',
            field=models.ManyToManyField(blank=True, null=True, to='skills.Skill', related_name='users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='working_hours',
            field=models.PositiveIntegerField(default=8),
            preserve_default=True,
        ),
    ]
