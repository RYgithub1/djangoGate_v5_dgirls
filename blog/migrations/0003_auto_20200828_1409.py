# Generated by Django 2.2.15 on 2020-08-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='サムネイル'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='動画'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='強み'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='名前'),
        ),
    ]
