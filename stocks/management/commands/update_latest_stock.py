from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist, ValidationError

from datetime import datetime
import json
import requests
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from cores.models import Config
from stocks.models import (
    Stock,
    CompanyHistoricalQuote,
    Company,
    DecisiveIndex,
    Latest,
    LatestFinancialInfo
)
from stocks.serializers import (
    StockSerializer,
    StockScanSerializer,
    CompanyHistoricalQuoteSerializer,
    DecisiveIndexSerializer
)


from stocks.models import Stock

User = get_user_model()


class Command(BaseCommand):
    help = 'Update latest stock'
   

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start update latest stock'))
        
        Latest.objects.all().delete()
        try:
            last_updated_date_instance = Config.objects.get(key='LAST_UPDATED_HISTORICAL_QUOTES')
        except Config.DoesNotExist:
            last_updated_date_instance = None

        if last_updated_date_instance is None:
            return

        last_update_date = last_updated_date_instance.value

        list_create = []
        for i in Stock.objects.filter(IsStrong=True).values_list('id', flat=True):
            xxx = CompanyHistoricalQuote.objects.filter(Stock_id=i).order_by('-Date')[:30]

            l = list(xxx.values_list('DealVolume', flat=True))
            float_l = [float(x) for x in l]
            sum_l = sum(float_l)
            average_volume_30 = round(sum_l/30)
            
            yyy = LatestFinancialInfo.objects.get(Stock_id=i)
            
            today_capital = xxx[0].DealVolume * xxx[0].PriceClose
            price_change = round((xxx[0].PriceClose - xxx[1].PriceClose) * 100 / xxx[0].PriceClose, 2)
            market_cap = yyy.MarketCapitalization
            deal_volume = xxx[0].DealVolume
            list_create.append(Latest(
                Stock_id=i,
                TodayCapital=today_capital,
                PriceChange=price_change,
                MarketCap=market_cap,
                DealVolume=deal_volume,
                AverageVolume30=average_volume_30
            ))
        print(len(list_create))

        Latest.objects.bulk_create(list_create)
        

        # Get stock id 
        # Get all price data of that stock id
        # Filter by current year
        # sort
        # Get current count

        self.stdout.write(self.style.SUCCESS('End update latest stock'))
