# Generated by Django 4.1.4 on 2023-05-09 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_slugs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='img_post',
        ),
    ]