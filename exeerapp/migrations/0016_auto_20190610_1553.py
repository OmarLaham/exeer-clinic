# Generated by Django 2.2 on 2019-06-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exeerapp', '0015_auto_20190610_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpguidesnippets',
            name='content_ar',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='helpguidesnippets',
            name='content_en',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='audio_url',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='video_url',
            field=models.CharField(max_length=254),
        ),
    ]
