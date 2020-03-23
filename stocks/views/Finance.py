import json
import requests
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from stocks.serializers import (
    LatestFinancialInfoSerializer,
    YearlyFinancialInfoSerializer,
    QuarterlyFinancialInfoSerializer,
    LastestFinancialReportsSerializer,
    LastestFinancialReportsNameSerializer,
    LastestFinancialReportsValueSerializer
)
from stocks.models import (
    Stock,
    LatestFinancialInfo, 
    YearlyFinancialInfo,
    QuarterlyFinancialInfo,
    LastestFinancialReportsName,
    LastestFinancialReportsValue
)

def mapData(data, type):
    result = []
    for item in data:
        for valuesItem in item['Values']:
            valuesItem['ID'] = item['ID']
            valuesItem['Type'] = type
            result.append(valuesItem)
    return result

def mapDataLastestFinancialReportsName(data):
    return data


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


class QuarterlyFinancialInfoRetrieveAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        # Miss api to handle fromYear && toYear
        fromYear = request.GET.get('fromYear')
        toYear = request.GET.get('toYear')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = QuarterlyFinancialInfo.objects.filter(Stock_id=filterStocks[0].id)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = QuarterlyFinancialInfoSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuarterlyFinancialInfoUpdateAPIView(UpdateAPIView):
    serializer_class = QuarterlyFinancialInfoSerializer

    def get_queryset(self):
        return QuarterlyFinancialInfo.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Finance/QuarterlyFinancialInfo"

        querystring = {
            "symbol": Symbol,
            "fromYear": "2016",
            "fromQuarter": "1",
            "toYear": "2019",
            "toQuarter": "4"
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()
        filteredStock = Stock.objects.filter(Symbol=Symbol)
        if filteredStock.count() != 1:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        QuarterlyFinancialInfo.objects.filter(Stock_id=filteredStock[0].id).delete()
        serializer = QuarterlyFinancialInfoSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class LastestFinancialReportsRetrieveAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        type = request.GET.get('type')
        year = request.GET.get('year')
        quarter = request.GET.get('quarter')
        count = request.GET.get('count')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = LastestFinancialReportsName.objects.filter(Type=type)
        query = LastestFinancialReportsValue.objects.filter(Stock_id=filterStocks[0].id)

        if result.count() == 0:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        print(203, type)
        serializer = LastestFinancialReportsSerializer(result, context={'year': year, 'quarter': quarter, 'type': type}, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LastestFinancialReportsNameUpdateAPIView(UpdateAPIView):
    def get_queryset(self):
        return LastestFinancialReports.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        type = request.GET.get('type')
        year = request.GET.get('year')
        quarter = request.GET.get('quarter')
        count = request.GET.get('count')
        if not Symbol or not type or not year or not quarter or not count:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialReports"

        querystring = {
            "symbol": Symbol,
            "type": type,
            "year": year,
            "quarter": quarter,
            "count": count
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()

        LastestFinancialReportsName.objects.filter(Type=type).delete()
        
        serializer = LastestFinancialReportsNameSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(Type=type)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class LastestFinancialReportsValueUpdateAPIView(UpdateAPIView):
    def get_queryset(self):
        return LastestFinancialReports.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        type = request.GET.get('type')
        year = request.GET.get('year')
        quarter = request.GET.get('quarter')
        count = request.GET.get('count')
        if not Symbol or not type or not year or not quarter or not count:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialReports"

        querystring = {
            "symbol": Symbol,
            "type": type,
            "year": year,
            "quarter": quarter,
            "count": count
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()

        if not data:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        filteredStock = Stock.objects.filter(Symbol=Symbol)
        if filteredStock.count() != 1:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        mappedData = mapData(data, type)


        serializer = LastestFinancialReportsValueSerializer(data=mappedData, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)

