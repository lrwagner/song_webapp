# Generated by Django 3.1 on 2020-08-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_request', '0003_auto_20200812_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='archive',
            field=models.BooleanField(default=0, verbose_name='Archivsong'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(default=0, verbose_name='Lyrics'),
            preserve_default=False,
        ),
    ]
