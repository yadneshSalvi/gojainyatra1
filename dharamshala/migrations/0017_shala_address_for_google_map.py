# Generated by Django 2.2.2 on 2019-07-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0016_auto_20190630_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='shala',
            name='address_for_google_map',
            field=models.CharField(default='India', max_length=500),
        ),
    ]
