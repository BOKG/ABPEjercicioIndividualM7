# Generated by Django 4.2.2 on 2023-06-28 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_task_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]