# Generated by Django 2.2.4 on 2022-07-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='profile_pics/ha.jpg', upload_to='profile_pics/'),
        ),
    ]
