import json
import requests
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from stocks.models import Stock
from stocks.serializers import StockSerializer

class StockAPIView(ListAPIView):
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
