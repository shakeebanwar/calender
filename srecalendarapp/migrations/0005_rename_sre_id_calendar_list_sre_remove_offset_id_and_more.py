# Generated by Django 4.1 on 2022-09-03 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srecalendarapp', '0004_list_type_calendar_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar_list',
            old_name='sre_id',
            new_name='sre',
        ),
        migrations.RemoveField(
            model_name='offset',
            name='id',
        ),
        migrations.AddField(
            model_name='offset',
            name='offset_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offset',
            name='offset_expiring',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offset',
            name='offset_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offset',
            name='offset_total',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offset',
            name='offset_used',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendar_list',
            name='calendar_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='calendar_list',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='offset',
            name='offset_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
