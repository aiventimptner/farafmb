# Generated by Django 3.1.4 on 2021-03-03 23:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_document_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254, null=True)),
                ('course', models.CharField(max_length=150)),
                ('lecturer', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='protocols', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
