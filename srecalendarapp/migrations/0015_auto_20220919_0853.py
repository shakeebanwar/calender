# Generated by Django 2.2 on 2022-09-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srecalendarapp', '0014_auto_20220916_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offset',
            name='offset_expiring',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
