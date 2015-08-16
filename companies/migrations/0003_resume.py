# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150812_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_applicant', models.CharField(max_length=30)),
                ('cv_applicant', models.CharField(max_length=200)),
                ('status_application', models.CharField(max_length=30)),
                ('company_applied', models.ForeignKey(to='companies.Company')),
            ],
        ),
    ]
