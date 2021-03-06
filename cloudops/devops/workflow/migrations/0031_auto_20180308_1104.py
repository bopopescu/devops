# Generated by Django 2.0.1 on 2018-03-08 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0030_auto_20180307_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applicant_project', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='项目经理'),
        ),
    ]
