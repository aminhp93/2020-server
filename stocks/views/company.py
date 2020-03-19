import json
import requests
from django.http import JsonResponse
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
    CompanySerializer,
    SubCompanySerializer,
    CompanyOfficerSerializer,
    CompanyTransactionSerializer
)
from stocks.models import (
    Company,
    SubCompany,
    Stock,
    CompanyOfficer,
    CompanyTransaction
)

class CompanyListAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        result = Company.objects.filter(Symbol=Symbol)
        if result.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(result[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyUpdateAPIView(UpdateAPIView):
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


class CompanyOfficerAPIView(RetrieveAPIView):
    def get_queryset(self):
        return CompanyOfficer.objects.all()

    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = CompanyOfficer.objects.filter(Stock_id=filterStocks[0].id)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyOfficerSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyOfficerUpdateAPIView(UpdateAPIView):
    def get_queryset(self):
        return CompanyOfficer.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Companies/CompanyOfficers"

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
        CompanyOfficer.objects.filter(Stock_id=filteredStock[0].id).delete()
        serializer = CompanyOfficerSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class CompanyTransactionsAPIView(RetrieveAPIView):
    def get_queryset(self):
        return CompanyTransaction.objects.all()

    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        filterStocks = Stock.objects.filter(Symbol=Symbol)
        if filterStocks.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        result = CompanyTransaction.objects.filter(Stock_id=filterStocks[0].id)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyTransactionSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyTransactionsUpdateAPIView(UpdateAPIView):
    def get_queryset(self):
        return CompanyTransaction.objects.all()

    def put(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        if not Symbol:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        url = "https://svr1.fireant.vn/api/Data/Companies/CompanyTransactions"

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
        CompanyTransaction.objects.filter(Stock_id=filteredStock[0].id).delete()
        serializer = CompanyTransactionSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(Stock=filteredStock[0])
        return Response(serializer.data, status = status.HTTP_201_CREATED)



