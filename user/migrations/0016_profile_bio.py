# Generated by Django 4.2.7 on 2023-11-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='no bio', max_length=200),
        ),
    ]
