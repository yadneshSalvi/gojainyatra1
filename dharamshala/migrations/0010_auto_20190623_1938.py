# Generated by Django 2.2.2 on 2019-06-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0009_auto_20190622_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Number_of_adults',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='Number_of_children',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
