# Generated by Django 3.0.2 on 2020-04-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200418_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='title'),
        ),
    ]
