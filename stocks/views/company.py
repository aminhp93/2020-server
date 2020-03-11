import json
import requests
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from stocks.serializers import CompanySerializer
from stocks.models import Company
from django.shortcuts import get_object_or_404
from rest_framework import status


class CompanyListAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        result = Company.objects.filter(Symbol=Symbol)
        if result.count() == 0:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(result[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CompanyUpdateAPIView(UpdateAPIView):
    serializer_class = CompanySerializer
    lookup_field = 'symbol'

    def get_queryset(self):
        return Company.objects.all()

    def put(self, request, *args, **kwargs):
        url = "https://svr1.fireant.vn/api/Data/Companies/CompanyInfo"

        querystring = {"symbol":"FPT"}

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        Symbol = request.GET.get('symbol')
        
        
        count = Company.objects.filter(Symbol=Symbol).count()
        if count == 0:
            serializer = CompanySerializer(data=response.json())    
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            created_company = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # serializer = self.get_serializer(instance, )
        
        return Response({'put': '123'})


class SubCompanyAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):

        url = "https://svr1.fireant.vn/api/Data/Companies/SubCompanies"

        querystring = {"symbol":"FPT"}

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        # print(response.json(), dir(response))
        return Response(response.json())