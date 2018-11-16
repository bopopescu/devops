# Generated by Django 2.0.1 on 2018-03-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksheet', '0004_auto_20180328_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='submitter_userid',
            field=models.CharField(default='', max_length=64, verbose_name='提交人'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='have_power_change',
            field=models.BooleanField(default=False, verbose_name='是否需要抄送邮箱'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='status',
            field=models.IntegerField(choices=[(0, '关闭'), (4, '待审批'), (1, '未受理'), (2, '待处理'), (3, '已处理')], verbose_name='状态'),
        ),
    ]
