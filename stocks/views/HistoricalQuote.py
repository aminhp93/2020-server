import json
import requests
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from django.http import JsonResponse


class HistoricalQuoteAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):

        url = "https://svr1.fireant.vn/api/Data/Companies/HistoricalQuotes"

        querystring = {
            "symbol": "FPT",
            "startDate": "2020-1-22",
            "endDate": "2020-2-22"
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        # print(response.text, dir(response))
        return Response(json.loads(response.text))