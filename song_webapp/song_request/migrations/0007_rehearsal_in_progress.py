# Generated by Django 3.1 on 2020-08-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_request', '0006_auto_20200816_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='rehearsal',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
    ]
