# Generated by Django 3.1.1 on 2020-09-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200913_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='key',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
