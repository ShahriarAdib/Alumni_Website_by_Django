# Generated by Django 2.1.1 on 2019-02-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0003_user_signup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_signup',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='Profile_image'),
        ),
    ]
