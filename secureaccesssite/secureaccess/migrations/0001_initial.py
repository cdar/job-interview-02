# Generated by Django 2.2.1 on 2019-05-27 15:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shareable_link', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('file', models.FileField(null=True, upload_to='')),
                ('url', models.URLField(null=True)),
                ('accessed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]