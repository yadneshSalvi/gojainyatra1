# Generated by Django 2.2.1 on 2019-05-21 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
