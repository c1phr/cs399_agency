# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyProject', '0002_share_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share_form',
            old_name='reciever_phone',
            new_name='receiver_phone',
        ),
    ]
