from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Q, F

from stocks.models import (
    Latest
)

from stocks.serializers import (
    LatestSerializer
)

class LatestViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Latest.objects.all()
        serializer = LatestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # ins = get_object_or_404(Latest, pk=pk)
        # serializer = LatestSerializer(ins)
        # return Response(serializer.data)
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        # stock = get_object_or_404(Stock, pk=pk)
        # serializer = StockSerializer(stock, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)
        pass

    def post(self, request):
        today = datetime.today().strftime('%Y-%m-%d') + 'T00:00:00Z'

        Symbol = request.data.get('Symbol', '')
        TodayCapital = request.data.get('TodayCapital', 5000000000)
        StartDate = request.data.get('startDate', today)
        EndDate = request.data.get('endDate', today)
        MinPrice = request.data.get('MinPrice', 0)
        IsVN30 = request.data.get('IsVN30', False)
        IsFavorite = request.data.get('IsFavorite', False)
        IsBlackList = request.data.get('IsBlackList', False)
        ICBCode = request.data.get('ICBCode')
        ChangePrice = request.data.get('ChangePrice')
        checkBlackList = request.data.get('checkBlackList')
        checkStrong = request.data.get('checkStrong')
        IsOnStudy = request.data.get('IsOnStudy', False)

        queryset = Latest.objects.filter(
            Q(PriceChange__gt=ChangePrice)\
            & Q(TodayCapital__gt=TodayCapital)
        )

        serializer = LatestSerializer(queryset, many=True)
        return Response(serializer.data)