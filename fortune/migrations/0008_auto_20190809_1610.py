# Generated by Django 2.2.3 on 2019-08-09 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0007_remove_fortune_entries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fortune',
            name='calcuate',
        ),
        migrations.AddField(
            model_name='fortune',
            name='calcuatetime',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
