# Generated by Django 2.1.1 on 2019-02-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_signup',
            name='id',
        ),
        migrations.AddField(
            model_name='user_signup',
            name='Id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
