# Generated by Django 2.1.7 on 2019-03-26 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_post_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]