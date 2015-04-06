# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0002_phase_project'),
        ('skills', '0002_skillinphase'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='skills',
            field=models.ManyToManyField(related_name='phases', blank=True, through='skills.SkillInPhase', null=True, to='skills.Skill'),
            preserve_default=True,
        ),
    ]
