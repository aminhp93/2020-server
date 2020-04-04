import json
import requests
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from cores.models import Config
from stocks.models import (
    Stock,
    CompanyHistoricalQuote,
    Company
)
from stocks.serializers import (
    StockSerializer,
    CompanyHistoricalQuoteSerializer
)

class StockAPIView(ListAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = StockSerializer(Stock.objects.all(), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        url = "https://svr3.fireant.vn/api/Data/Markets/TradingStatistic"

        headers = {
            'cache-control': 'no-cache'
        }

        response = requests.request('GET', url, headers=headers)
        Stock.objects.all().delete()
        serializer = StockSerializer(data=response.json(), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        created = serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class StockFilterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        ICBCode = request.data.get('ICBCode')
        Date = request.data.get('Date')
        
        if not ICBCode and not Date:
            return Response({'Error': 'No ICBCode and Date'})
        result = []
        if ICBCode and Date:
            filteredCompany = Company.objects.filter(ICBCode=ICBCode)
            filteredStocks = Stock.objects.filter(Symbol__in=[i.Symbol for i in filteredCompany])
            result = CompanyHistoricalQuote.objects.filter(Q(Date=Date) & Q(Stock_id__in=[i.id for i in filteredStocks]))
        if Date and not ICBCode:
            result = CompanyHistoricalQuote.objects.filter(Q(Date=Date))
        
        serializer = CompanyHistoricalQuoteSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

