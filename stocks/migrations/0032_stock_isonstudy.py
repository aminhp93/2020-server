# Generated by Django 3.0.2 on 2020-09-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0031_stock_isstrong'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='IsOnStudy',
            field=models.BooleanField(default=False, verbose_name='IsOnStudy'),
        ),
    ]