# Generated by Django 4.1.3 on 2022-12-18 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangaRoll_app', '0007_remove_manga_pdfs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='images',
            new_name='manga_images',
        ),
    ]
