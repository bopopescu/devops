# Generated by Django 2.0 on 2018-03-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0042_merge_20180318_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronflow',
            name='describe',
            field=models.TextField(max_length=1000, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='cronflow',
            name='execute_time',
            field=models.DateTimeField(null=True, verbose_name='执行时间'),
        ),
    ]
