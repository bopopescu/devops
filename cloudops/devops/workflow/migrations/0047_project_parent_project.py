# Generated by Django 2.0.1 on 2018-03-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0046_project_releaseflow_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parent_project',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='父项目'),
        ),
    ]
