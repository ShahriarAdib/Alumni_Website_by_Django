# Generated by Django 2.1.1 on 2019-02-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0007_auto_20190213_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
