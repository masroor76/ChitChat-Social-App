# Generated by Django 5.2 on 2025-04-22 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_likedposts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_likes',
        ),
    ]
