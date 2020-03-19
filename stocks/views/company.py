import json
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from stocks.serializers import CompanySerializer, SubCompanySerializer
from stocks.models import Company, SubCompany, Stock


class CompanyListAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        result = Company.objects.filter(Symbol=Symbol)
        if result.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(result[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyUpdateAPIView(UpdateAPIView):
    serializer_class = CompanySerializer
    lookup_field = 'symbol'

    def get_queryset(self):
        return Company.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Companies/CompanyInfo"

        querystring = {
            "symbol": Symbol
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)        
        
        Company.objects.filter(Symbol=Symbol).delete()
        
        serializer = CompanySerializer(data=response.json())
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class SubCompanyAPIView(RetrieveAPIView):
    def get_queryset(self):
        return SubCompany.objects.all()

    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = SubCompany.objects.filter(Stock_id=filterStocks[0].id)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = SubCompanySerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubCompanyUpdateAPIView(UpdateAPIView):
    serializer_class = SubCompanySerializer
    lookup_field = 'symbol'

    def get_queryset(self):
        return SubCompany.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Companies/SubCompanies"

        querystring = {
            "symbol": Symbol
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)        
        
        data = response.json()
        filteredStock = Stock.objects.filter(Symbol=Symbol)
        if filteredStock.count() != 1:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        SubCompany.objects.filter(Stock_id=filteredStock[0].id).delete()
        serializer = SubCompanySerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)