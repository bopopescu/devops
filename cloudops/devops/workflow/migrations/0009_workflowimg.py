# Generated by Django 2.0.1 on 2018-02-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_auto_20180225_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkFlowIMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(upload_to='./img')),
            ],
            options={
                'db_table': 'workflow_img',
            },
        ),
    ]
