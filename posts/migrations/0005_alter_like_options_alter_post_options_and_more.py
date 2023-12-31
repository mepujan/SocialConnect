# Generated by Django 4.2.7 on 2023-11-07 00:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ('-updated',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
