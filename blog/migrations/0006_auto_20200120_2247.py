# Generated by Django 2.2.9 on 2020-01-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_is_publish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='massage',
            new_name='message',
        ),
    ]
