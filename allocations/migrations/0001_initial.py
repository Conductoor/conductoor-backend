# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0004_auto_20150331_1402'),
        ('skills', '0003_auto_20150331_1402'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('phase', models.ForeignKey(to='phases.Phase', related_name='allocations')),
                ('skill', models.ForeignKey(to='skills.Skill', related_name='allocations')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='allocations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
