# Generated by Django 2.2 on 2021-11-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20211117_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='position',
            field=models.TextField(default=''),
        ),
    ]
