# Generated by Django 2.0.1 on 2018-03-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0027_auto_20180307_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_userflow',
            name='status',
            field=models.IntegerField(choices=[(0, '不通过'), (1, '未审批'), (9, '通过')], verbose_name='状态'),
        ),
    ]
