# Generated by Django 2.2.4 on 2022-07-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0016_remove_photo_profile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='img',
        ),
    ]
