# Generated by Django 2.2.9 on 2020-01-20 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_publish',
        ),
    ]
