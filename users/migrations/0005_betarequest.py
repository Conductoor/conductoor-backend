# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150523_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetaRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(blank=True, null=True, max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
