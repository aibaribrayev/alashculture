# Generated by Django 2.2 on 2021-11-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
    ]
