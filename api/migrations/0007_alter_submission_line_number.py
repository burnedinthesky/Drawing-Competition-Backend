# Generated by Django 4.2.13 on 2024-05-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_round_end_time_alter_round_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='line_number',
            field=models.IntegerField(default=0, verbose_name='單字數'),
        ),
    ]
