# Generated by Django 2.1.1 on 2019-02-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0002_auto_20190207_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_signup',
            name='image',
            field=models.ImageField(blank=True, upload_to='Profile_image'),
        ),
    ]
