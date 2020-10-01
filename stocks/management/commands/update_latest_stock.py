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
    Latest
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
        for i in Stock.objects.values_list('id', flat=True):
            ins = CompanyHistoricalQuote.objects.get(Stock_id=i, Date=last_update_date)

            today_capital = 1
            percent_change = 1
            market_cap = 1
            deal_volume = 1
            list_create.append(Latest(
                Stock_id=i,
                TodayCapital=today_capital,
                PercentChange=percent_change,
                MarketCap=market_cap,
                DealVolume=deal_volume
            ))
        # [Latest(Stock_id=i) for i in Stock.objects.values_list('id', flat=True)]

        # print(Stock.objects.values_list('id', flat=True))
        Latest.objects.bulk_create(list_create)
        
        self.stdout.write(self.style.SUCCESS('End update latest stock'))
