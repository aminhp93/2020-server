import json
import requests
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class AllNewsApiView(APIView):
    def get(self, request, *args, **kwargs):
        startIndex = request.GET.get('startIndex')
        count = request.GET.get('count')

        url = 'https://svr4.fireant.vn/api/Data/News/AllNews'

        querystring = {
            "startIndex": startIndex,
            "count": count
        }

        headers = {
            'cache-control': 'no-cache'
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        if not data or response.status_code != 200:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)


class PositiveNewsApiView(APIView):
    def get(self, request, *args, **kwargs):
        startIndex = request.GET.get('startIndex')
        count = request.GET.get('count')

        url = 'https://svr4.fireant.vn/api/Data/News/PositiveNews'

        querystring = {
            "startIndex": startIndex,
            "count": count
        }

        headers = {
            'cache-control': 'no-cache'
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        if not data or response.status_code != 200:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)


class NegativeNewsApiView(APIView):
    def get(self, request, *args, **kwargs):
        startIndex = request.GET.get('startIndex')
        count = request.GET.get('count')

        url = 'https://svr4.fireant.vn/api/Data/News/NegativeNews'

        querystring = {
            "startIndex": startIndex,
            "count": count
        }

        headers = {
            'cache-control': 'no-cache'
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        if not data or response.status_code != 200:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)


class NewsInGroupApiView(APIView):
    def get(self, request, *args, **kwargs):
        startIndex = request.GET.get('startIndex')
        count = request.GET.get('count')
        group = request.GET.get('group')

        url = 'https://svr4.fireant.vn/api/Data/News/NewsInGroup'

        querystring = {
            "group": group,
            "startIndex": startIndex,
            "count": count
        }

        headers = {
            'cache-control': 'no-cache'
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()

        if not data or response.status_code != 200:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)