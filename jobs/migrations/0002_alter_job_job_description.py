# Generated by Django 3.2.9 on 2021-12-05 15:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
