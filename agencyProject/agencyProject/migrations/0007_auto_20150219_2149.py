# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyProject', '0006_auto_20150219_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewform',
            name='review',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
    ]
