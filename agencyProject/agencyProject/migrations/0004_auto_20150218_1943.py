# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyProject', '0003_auto_20150218_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share_form',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='share_form',
            name='last_name',
        ),
    ]
