import json
import requests
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from stocks.serializers import LatestFinancialInfoSerializer, YearlyFinancialInfoSerializer
from stocks.models import (
    Stock,
    LatestFinancialInfo, 
    YearlyFinancialInfo
)


class LatestFinancialInfoRetrieveAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        result = LatestFinancialInfo.objects.filter(Symbol=Symbol)
        if result.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = LatestFinancialInfoSerializer(result[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LatestFinancialInfoUpdateAPIView(UpdateAPIView):
    serializer_class = LatestFinancialInfoSerializer

    def get_queryset(self):
        return LatestFinancialInfo.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialInfo"

        querystring = {
            "symbol": Symbol 
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        LatestFinancialInfo.objects.filter(Symbol=Symbol).delete()
        
        serializer = LatestFinancialInfoSerializer(data=response.json())
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class YearlyFinancialInfoRetrieveAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        # Miss api to handle fromYear && toYear
        fromYear = request.GET.get('fromYear')
        toYear = request.GET.get('toYear')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = YearlyFinancialInfo.objects.filter(Stock_id=filterStocks[0].id)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = YearlyFinancialInfoSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class YearlyFinancialInfoUpdateAPIView(UpdateAPIView):
    serializer_class = YearlyFinancialInfoSerializer

    def get_queryset(self):
        return YearlyFinancialInfo.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Finance/YearlyFinancialInfo"

        querystring = {
            "symbol": Symbol,
            "fromYear": "2016",
            "toYear": "2019"
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()
        filteredStock = Stock.objects.filter(Symbol=Symbol)
        if filteredStock.count() != 1:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        YearlyFinancialInfo.objects.filter(Stock_id=filteredStock[0].id).delete()
        serializer = YearlyFinancialInfoSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)