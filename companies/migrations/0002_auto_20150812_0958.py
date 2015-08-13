# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='job_description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='job_requirement',
        ),
        migrations.RemoveField(
            model_name='company',
            name='profile',
        ),
        migrations.AddField(
            model_name='company',
            name='comapany_profile',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='job_profile',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='job_requirements',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='job_title',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=60),
        ),
        migrations.AddField(
            model_name='company',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='vacancies',
            field=models.IntegerField(default=0),
        ),
    ]
