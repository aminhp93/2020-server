import json
import requests
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from rest_framework.response import Response
from rest_framework import status

from stocks.serializers import (
    CompanyHistoricalQuoteSerializer
)
from stocks.models import (
    CompanyHistoricalQuote
)


class AnalysisListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        Date = request.GET.get('Date')
        data = CompanyHistoricalQuote.objects.filter(Date=Date)
        serializer = CompanyHistoricalQuoteSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StockNewsAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'Sec-Fetch-Dest': 'empty',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://finance.vietstock.vn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://finance.vietstock.vn/MBB-ngan-hang-tmcp-quan-doi.htm',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        }

        data = {
            'type': '1',
            'pageSize': '20'
        }

        response = requests.post('https://finance.vietstock.vn/data/headernews', headers=headers, data=data)
        print(response)
        return Response(response.json(), status=status.HTTP_200_OK)