# Generated by Django 3.2.9 on 2021-12-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211130_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(default='rohitgeddam2018@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]