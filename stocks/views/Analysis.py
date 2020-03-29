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
    AnalysisSerializer
)
from stocks.models import (
    CompanyHistoricalQuote
)


class AnalysisListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        Date = request.GET.get('Date')
        Date = Date + 'T00:00:00Z'
        # 2020-03-29T00:00:00Z
        data = CompanyHistoricalQuote.objects.filter(Date=Date)
        serializer = AnalysisSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
