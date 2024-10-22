# Generated by Django 3.2.9 on 2021-11-28 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_rename_noticeclass_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='files',
        ),
        migrations.AddField(
            model_name='notice',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notice',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='NoticeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/files')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notices.notice')),
            ],
        ),
    ]
