# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='recruiter_id',
            field=models.IntegerField(default=0),
        ),
    ]
