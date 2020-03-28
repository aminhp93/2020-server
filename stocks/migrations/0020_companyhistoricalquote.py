# Generated by Django 3.0.2 on 2020-03-28 10:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0019_lastestfinancialreportsname_industrytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyHistoricalQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('Date', models.CharField(blank=True, max_length=255, verbose_name='Date')),
                ('PriceHigh', models.FloatField(blank=True, null=True, verbose_name='PriceHigh')),
                ('PriceLow', models.FloatField(blank=True, null=True, verbose_name='PriceLow')),
                ('PriceOpen', models.FloatField(blank=True, null=True, verbose_name='PriceOpen')),
                ('PriceAverage', models.FloatField(blank=True, null=True, verbose_name='PriceAverage')),
                ('PriceClose', models.FloatField(blank=True, null=True, verbose_name='PriceClose')),
                ('PricePreviousClose', models.FloatField(blank=True, null=True, verbose_name='PricePreviousClose')),
                ('PriceBasic', models.FloatField(blank=True, null=True, verbose_name='PriceBasic')),
                ('TotalVolume', models.FloatField(blank=True, null=True, verbose_name='TotalVolume')),
                ('DealVolume', models.FloatField(blank=True, null=True, verbose_name='DealVolume')),
                ('Volume', models.FloatField(blank=True, null=True, verbose_name='Volume')),
                ('PutthroughVolume', models.FloatField(blank=True, null=True, verbose_name='PutthroughVolume')),
                ('TotalTrade', models.FloatField(blank=True, null=True, verbose_name='TotalTrade')),
                ('TotalValue', models.FloatField(blank=True, null=True, verbose_name='TotalValue')),
                ('PutthroughValue', models.FloatField(blank=True, null=True, verbose_name='PutthroughValue')),
                ('BuyForeignQuantity', models.FloatField(blank=True, null=True, verbose_name='BuyForeignQuantity')),
                ('BuyForeignValue', models.FloatField(blank=True, null=True, verbose_name='BuyForeignValue')),
                ('SellForeignQuantity', models.FloatField(blank=True, null=True, verbose_name='SellForeignQuantity')),
                ('SellForeignValue', models.FloatField(blank=True, null=True, verbose_name='SellForeignValue')),
                ('BuyCount', models.FloatField(blank=True, null=True, verbose_name='BuyCount')),
                ('BuyQuantity', models.FloatField(blank=True, null=True, verbose_name='BuyQuantity')),
                ('SellCount', models.FloatField(blank=True, null=True, verbose_name='SellCount')),
                ('SellQuantity', models.FloatField(blank=True, null=True, verbose_name='SellQuantity')),
                ('BuyAvg', models.FloatField(blank=True, null=True, verbose_name='BuyAvg')),
                ('SellAvg', models.FloatField(blank=True, null=True, verbose_name='SellAvg')),
                ('AdjRatio', models.FloatField(blank=True, null=True, verbose_name='AdjRatio')),
                ('AdjClose', models.FloatField(blank=True, null=True, verbose_name='AdjClose')),
                ('AdjOpen', models.FloatField(blank=True, null=True, verbose_name='AdjOpen')),
                ('AdjHigh', models.FloatField(blank=True, null=True, verbose_name='AdjHigh')),
                ('AdjLow', models.FloatField(blank=True, null=True, verbose_name='AdjLow')),
                ('CurrentForeignRoom', models.FloatField(blank=True, null=True, verbose_name='CurrentForeignRoom')),
                ('Shares', models.FloatField(blank=True, null=True, verbose_name='Shares')),
                ('Exchange', models.FloatField(blank=True, null=True, verbose_name='Exchange')),
                ('PE', models.FloatField(blank=True, null=True, verbose_name='PE')),
                ('PS', models.FloatField(blank=True, null=True, verbose_name='PS')),
                ('PB', models.FloatField(blank=True, null=True, verbose_name='PB')),
                ('MarketCap', models.FloatField(blank=True, null=True, verbose_name='MarketCap')),
                ('LastUpdated', models.CharField(blank=True, max_length=255, null=True, verbose_name='LastUpdated')),
                ('Stock', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='CompanyHistoricalQuote_Stock', to='stocks.Stock')),
            ],
            options={
                'verbose_name': 'CompanyHistoricalQuote',
                'verbose_name_plural': 'CompanyHistoricalQuote',
                'ordering': ('-created', '-id'),
            },
        ),
    ]
