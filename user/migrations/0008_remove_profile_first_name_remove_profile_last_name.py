# Generated by Django 4.2.7 on 2023-11-06 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
