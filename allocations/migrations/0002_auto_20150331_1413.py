# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='phase',
            field=models.ForeignKey(related_name='allocations', to='phases.Phase', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='allocation',
            name='skill',
            field=models.ForeignKey(related_name='allocations', to='skills.Skill', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='allocation',
            name='user',
            field=models.ForeignKey(related_name='allocations', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
    ]
