# Generated by Django 4.1 on 2022-08-31 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srecalendarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset_id', models.IntegerField()),
            ],
        ),
    ]
