# Generated by Django 3.0.2 on 2020-09-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0030_remove_stock_isstrong'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='IsStrong',
            field=models.BooleanField(default=True, verbose_name='IsStrong'),
        ),
    ]