# Generated by Django 3.0.2 on 2020-09-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0027_stock_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='IsStrong',
            field=models.BooleanField(default=False, verbose_name='IsStrong'),
        ),
    ]
