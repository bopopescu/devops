# Generated by Django 2.0.1 on 2018-03-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0024_auto_20180305_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_user',
            name='name',
            field=models.CharField(max_length=24, null=True, verbose_name='名字'),
        ),
    ]
