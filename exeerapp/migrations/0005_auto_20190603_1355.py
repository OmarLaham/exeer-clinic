# Generated by Django 2.2 on 2019-06-03 10:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exeerapp', '0004_auto_20190603_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content_ar',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='content_en',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
