# Generated by Django 4.2.4 on 2023-09-25 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='city',
            new_name='task',
        ),
        migrations.RemoveField(
            model_name='record',
            name='address',
        ),
        migrations.RemoveField(
            model_name='record',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='record',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='record',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.RemoveField(
            model_name='record',
            name='zipcode',
        ),
    ]