# Generated by Django 2.2.3 on 2019-08-08 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0002_auto_20190809_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortune',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fortune',
            name='datetime',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='fortune',
            name='finishtime',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]