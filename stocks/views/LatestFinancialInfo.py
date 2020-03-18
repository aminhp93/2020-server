import json
import requests
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from stocks.serializers import LatestFinancialInfoSerializer
from stocks.models import LatestFinancialInfo


class LatestFinancialInfoRetrieveAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        Symbol = request.GET.get('symbol')
        result = LatestFinancialInfo.objects.filter(Symbol=Symbol)
        if result.count() != 1:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        serializer = LatestFinancialInfoSerializer(result[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LatestFinancialInfoAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):

        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialInfo"

        querystring = {"symbol":"FPT"}

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        # print(response.text, dir(response))
        return Response(json.loads(response.text))


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