# Generated by Django 3.1 on 2020-08-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rehearsal',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['-band']},
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Titel'),
        ),
    ]