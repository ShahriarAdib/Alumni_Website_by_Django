# Generated by Django 2.1.1 on 2019-02-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0011_auto_20190218_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcoming_event',
            fields=[
                ('serial', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.CharField(max_length=500)),
                ('event_picture', models.ImageField(blank='True', upload_to='')),
            ],
        ),
    ]