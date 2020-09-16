from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
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
    DecisiveIndex
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
    help = 'Update 123'
   

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start update strong stock'))
        
        StartDate = "2020-09-14T00:00:00Z"
        EndDate = "2020-09-15T00:00:00Z"
        MinPrice = 0
        ChangePrice = -100
        TodayCapital = 1000000000
        
        filteredStocks = Stock.objects.all()

        companyHistoricalQuote = CompanyHistoricalQuote.objects\
            .filter(Stock_id__in=[i.id for i in filteredStocks])\
            .filter(Date=EndDate)\
            .filter(PriceClose__gt=MinPrice)\
            .annotate(TodayCapital=F('PriceClose') * F('DealVolume'))\
            .filter(TodayCapital__gt=TodayCapital)

        dic1 = CompanyHistoricalQuote.objects\
            .filter(Stock_id__in=[i.Stock_id for i in companyHistoricalQuote])\
            .filter(Date=EndDate)

        dic2 = CompanyHistoricalQuote.objects\
            .filter(Stock_id__in=[i.Stock_id for i in companyHistoricalQuote])\
            .filter(Date=StartDate)
        
        result = []
        for i in dic1:
            start = dic2.filter(Stock_id=i.Stock_id)
            if len(start) == 1:
                if (i.PriceClose - start[0].PriceClose)/ start[0].PriceClose * 100 > ChangePrice:
                    result.append(i.Stock_id)

        print(result, len(result))
        Stock.objects.filter(~Q(id__in=result)).update(IsStrong=False)
        
        self.stdout.write(self.style.SUCCESS('End update strong stock'))
