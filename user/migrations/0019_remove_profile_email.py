# Generated by Django 4.2.7 on 2023-11-08 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]