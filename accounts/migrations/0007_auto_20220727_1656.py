# Generated by Django 2.2.4 on 2022-07-27 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220727_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Accounts',
        ),
    ]
