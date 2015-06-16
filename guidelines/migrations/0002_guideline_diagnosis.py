# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0001_initial'),
        ('guidelines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideline',
            name='diagnosis',
            field=models.ManyToManyField(help_text=b'Canonical terms only', to='opal.Condition'),
            preserve_default=True,
        ),
    ]
