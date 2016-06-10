# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_aptitutest_eligtest_hrtest_quanttest_reasontest_techtest_verbtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.RemoveField(
            model_name='aptitutest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='aptitutest',
            name='test',
        ),
        migrations.DeleteModel(
            name='AptituTest',
        ),
    ]
