# Generated by Django 2.2.2 on 2019-08-23 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0020_auto_20190823_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='address',
            new_name='dharamshala_address',
        ),
    ]
