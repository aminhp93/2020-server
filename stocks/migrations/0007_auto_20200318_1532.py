# Generated by Django 3.0.2 on 2020-03-18 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Symbol',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='ICBCode'),
        ),
        migrations.AlterField(
            model_name='historicalquote',
            name='Symbol',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Symbol'),
        ),
        migrations.AlterField(
            model_name='intradayquote',
            name='Symbol',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Symbol'),
        ),
        migrations.AlterField(
            model_name='latestfinancialinfo',
            name='Symbol',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=255, unique=True, verbose_name='Symbol'),
            preserve_default=False,
        ),
    ]
