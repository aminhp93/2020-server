# Generated by Django 3.0.2 on 2020-03-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0017_auto_20200322_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastestfinancialreportsvalue',
            name='Type',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Type'),
        ),
    ]
