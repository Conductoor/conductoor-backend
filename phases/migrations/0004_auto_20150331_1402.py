# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0003_phase_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phase',
            old_name='skills',
            new_name='required_skills',
        ),
    ]
