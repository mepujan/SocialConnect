# Generated by Django 4.2.7 on 2023-11-08 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
