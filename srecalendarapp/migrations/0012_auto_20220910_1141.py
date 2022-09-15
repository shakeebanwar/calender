# Generated by Django 2.2 on 2022-09-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srecalendarapp', '0011_auto_20220910_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offset',
            name='offset_bal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offset',
            name='offset_expiring',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offset',
            name='offset_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offset',
            name='offset_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offset',
            name='offset_used',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
