# Generated by Django 4.2.3 on 2023-08-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisement', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='photo',
            field=models.ImageField(default=1, upload_to='advertisement', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
