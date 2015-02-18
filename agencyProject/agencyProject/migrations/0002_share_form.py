# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyProject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='share_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sender_email', models.EmailField(max_length=254)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('sender_phone', models.CharField(max_length=20)),
                ('reciever_phone', models.CharField(max_length=20)),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
