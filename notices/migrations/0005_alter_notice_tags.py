# Generated by Django 3.2.9 on 2021-11-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_yeartag_year'),
        ('notices', '0004_notice_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='tags',
            field=models.ManyToManyField(related_name='notices', to='core.YearTag'),
        ),
    ]
