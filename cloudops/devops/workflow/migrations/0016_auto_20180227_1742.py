# Generated by Django 2.0.1 on 2018-02-27 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0015_auto_20180227_1657'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='authority_flow',
            unique_together={('project', 'modify_user', 'applicationtime')},
        ),
    ]
