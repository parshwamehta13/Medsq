# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('profile', models.CharField(max_length=400)),
                ('vacancies', models.IntegerField()),
                ('job_description', models.CharField(max_length=400)),
                ('job_requirement', models.CharField(max_length=400)),
            ],
        ),
    ]
