# Generated by Django 2.0.1 on 2018-03-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0038_auto_20180308_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_user',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name='用户名'),
        ),
    ]
