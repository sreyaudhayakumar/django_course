# Generated by Django 4.2.3 on 2024-01-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
