# Generated by Django 3.0.8 on 2020-11-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20201109_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/user.png', null=True, upload_to='images'),
        ),
    ]