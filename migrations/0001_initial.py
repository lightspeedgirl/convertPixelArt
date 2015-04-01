# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('threadID', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('threadName', models.CharField(max_length=200)),
                ('red', models.IntegerField(default=0)),
                ('green', models.IntegerField(default=0)),
                ('blue', models.IntegerField(default=0)),
                ('threadHex', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
