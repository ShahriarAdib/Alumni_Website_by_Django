# Generated by Django 2.1.1 on 2019-02-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0005_auto_20190211_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete='user', to='alumni_app.user_signup')),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('post_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete='user', to='alumni_app.user_signup')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_no',
            field=models.ForeignKey(on_delete='post_no', to='alumni_app.post'),
        ),
    ]
