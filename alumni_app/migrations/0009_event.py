# Generated by Django 2.1.1 on 2019-02-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0008_auto_20190214_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_no', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.CharField(max_length=500)),
                ('event_picture', models.ImageField(blank='True', upload_to='')),
            ],
        ),
    ]