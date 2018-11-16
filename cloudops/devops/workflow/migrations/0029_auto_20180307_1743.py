# Generated by Django 2.0.1 on 2018-03-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0028_auto_20180307_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority_flow',
            name='status',
            field=models.IntegerField(choices=[(0, '不通过'), (1, '待审批'), (2, '待执行'), (3, '权限变更完成')], help_text='0 不通过, 1 待审批, 2 待执行, 3 已执行', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='project_releaseflow',
            name='status',
            field=models.IntegerField(choices=[(0, '不通过'), (1, '未审批'), (2, '测试审批通过'), (3, '项目经理审批通过'), (4, '待发布'), (9, '已发布')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='projectuserapplyflow',
            name='status',
            field=models.IntegerField(choices=[(0, '不通过'), (1, '待审批'), (2, '待执行'), (3, '执行完成')], verbose_name='状态'),
        ),
    ]