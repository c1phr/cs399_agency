# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyProject', '0005_review_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review_form',
            new_name='ReviewForm',
        ),
    ]
