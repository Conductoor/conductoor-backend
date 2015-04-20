# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0005_phase_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phase',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='phase',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
