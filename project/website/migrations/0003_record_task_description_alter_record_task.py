# Generated by Django 4.2.4 on 2023-09-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_city_record_task_remove_record_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='task_description',
            field=models.TextField(default='Unplanned goal pussy'),
        ),
        migrations.AlterField(
            model_name='record',
            name='task',
            field=models.CharField(max_length=200),
        ),
    ]