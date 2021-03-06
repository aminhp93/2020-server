# Generated by Django 3.0.2 on 2020-03-18 16:14

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_auto_20200318_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('Symbol', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Symbol')),
                ('InstitutionID', models.CharField(blank=True, max_length=255, verbose_name='InstitutionID')),
                ('Exchange', models.CharField(blank=True, max_length=255, verbose_name='Exchange')),
                ('CompanyName', models.CharField(blank=True, max_length=255, verbose_name='CompanyName')),
                ('ShortName', models.CharField(blank=True, max_length=255, verbose_name='ShortName')),
                ('InternationalName', models.CharField(blank=True, max_length=255, verbose_name='InternationalName')),
                ('CompanyProfile', models.CharField(blank=True, max_length=255, verbose_name='CompanyProfile')),
                ('Type', models.CharField(blank=True, max_length=255, verbose_name='Type')),
                ('Ownership', models.CharField(blank=True, max_length=255, verbose_name='Ownership')),
                ('Shares', models.CharField(blank=True, max_length=255, verbose_name='Shares')),
                ('IsListed', models.CharField(blank=True, max_length=255, verbose_name='IsListed')),
                ('CharterCapital', models.CharField(blank=True, max_length=255, verbose_name='CharterCapital')),
            ],
            options={
                'verbose_name': 'SubCompany',
                'verbose_name_plural': 'SubCompanies',
                'ordering': ('-created', '-id'),
            },
        ),
    ]
