# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_skillinphase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillinphase',
            old_name='amount',
            new_name='required_hours',
        ),
    ]
