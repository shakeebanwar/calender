# Generated by Django 4.1 on 2022-09-03 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srecalendarapp', '0005_rename_sre_id_calendar_list_sre_remove_offset_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offset',
            name='offset_end',
        ),
        migrations.RemoveField(
            model_name='offset',
            name='offset_expiring',
        ),
        migrations.RemoveField(
            model_name='offset',
            name='offset_start',
        ),
        migrations.RemoveField(
            model_name='offset',
            name='offset_total',
        ),
        migrations.RemoveField(
            model_name='offset',
            name='offset_used',
        ),
    ]