# Generated by Django 2.2 on 2019-06-03 10:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exeerapp', '0005_auto_20190603_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content_ar',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
