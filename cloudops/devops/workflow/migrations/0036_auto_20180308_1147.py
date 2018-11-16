# Generated by Django 2.0.1 on 2018-03-08 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0035_auto_20180308_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoritygroupchangelogs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cronflow',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='depart_director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='部门负责人'),
        ),
        migrations.AlterField(
            model_name='project',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=models.SET('已删除'), related_name='applicant_project', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(null=True, on_delete=models.SET('已删除'), to=settings.AUTH_USER_MODEL, verbose_name='项目经理'),
        ),
        migrations.AlterField(
            model_name='project_group',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='组成员'),
        ),
        migrations.AlterField(
            model_name='project_releaseflow',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AlterField(
            model_name='project_userflow',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant_projectuser', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
    ]
