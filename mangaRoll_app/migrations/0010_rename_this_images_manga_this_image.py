# Generated by Django 4.1.3 on 2022-12-18 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangaRoll_app', '0009_rename_manga_images_manga_this_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='this_images',
            new_name='this_image',
        ),
    ]
