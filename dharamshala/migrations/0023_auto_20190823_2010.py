# Generated by Django 2.2.2 on 2019-08-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0022_auto_20190823_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='phone_of_dharamshala_or_bunglow_or_sanatorium',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
    ]
