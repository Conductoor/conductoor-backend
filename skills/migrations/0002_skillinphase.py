# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0002_phase_project'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillInPhase',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('phase', models.ForeignKey(to='phases.Phase')),
                ('skill', models.ForeignKey(to='skills.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
