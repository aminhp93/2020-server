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
        
        StartDate = "2020-09-17T00:00:00Z"
        EndDate = "2020-09-18T00:00:00Z"
        MinPrice = 5000
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

        # print(len(result))

        queryset = Q(id__in=result) & Q(IsStrong=True)

        a = Stock.objects.filter(queryset)
        b = Stock.objects.exclude(queryset)
        # print(len(a), len(b))
        list_ids = a.values_list('id', flat=True)
        

        
        # a.update(IsStrong=True)
        # b.update(IsStrong=False)

        # Get ICBCode from list a
        c = Company.objects.filter(Stock__in=list_ids)
        
        d = c.values_list('ICBCode', flat=True)
        e = c.values('ICBCode', 'Stock')

        d = sorted(set(d))
        
        final = []
        for i in d:
            g = c.filter(ICBCode=i).values_list('Stock', flat=True)
            g = list(g)

            marketCap = CompanyHistoricalQuote.objects\
                .filter(Q(Stock__in=g) & Q(Date=EndDate))\
                .values('Stock', 'MarketCap')
            marketCap = list(marketCap)
            marketCap = sorted(marketCap, key=lambda i: i["MarketCap"], reverse=True)
            x = slice(5)
            
            h = marketCap[x]
            j = [i["Stock"] for i in h]

            final = final + j

        queryset = Q(id__in=final)


        include = Stock.objects.filter(queryset)
        exclude = Stock.objects.exclude(queryset)

        include.update(IsStrong=True)
        exclude.update(IsStrong=False)



        
        self.stdout.write(self.style.SUCCESS('End update strong stock'))
