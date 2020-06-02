from django.db.models import Q
from rest_framework import serializers

from stocks.models import (
    Stock,
    Company,
    SubCompany,
    CompanyHistoricalQuote,
    CompanyOfficer,
    CompanyTransaction,
    YearlyFinancialInfo,
    QuarterlyFinancialInfo,
    LatestFinancialInfo,
    LastestFinancialReportsName,
    LastestFinancialReportsValue,
    DecisiveIndex
)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company

        fields = [
            'ICBCode',
            'Stock'
        ]


class SubCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCompany
        exclude = ['Stock']


class CompanyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOfficer
        exclude = ['Stock']


class CompanyHistoricalQuoteSerializer(serializers.ModelSerializer):
    TodayCapital = serializers.SerializerMethodField()
    PriceChange = serializers.SerializerMethodField()
    LastPrice = serializers.SerializerMethodField()
    CurrentRevenue = serializers.SerializerMethodField()
    LastRevenue = serializers.SerializerMethodField()
    RevenueChange = serializers.SerializerMethodField()

    def get_TodayCapital(self, obj):
        return obj.PriceClose * obj.DealVolume

    def get_LastPrice(self, obj):
        StartDate = self.context.get('StartDate')
        xxx = CompanyHistoricalQuote.objects.filter(Q(Date=StartDate) & Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].PriceClose
        return None

    def get_PriceChange(self, obj):
        StartDate = self.context.get('StartDate')
        xxx = CompanyHistoricalQuote.objects.filter(Q(Date=StartDate) & Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return (obj.PriceClose - xxx[0].PriceClose)/obj.PriceClose * 100
        return None

    def get_CurrentRevenue(self, obj):
        CurrentRevenue = self.context.get('CurrentRevenue')
        if not CurrentRevenue:
        # or obj.Stock_id != 3341:
            return None
        rev2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=1))
        if len(rev2019) == 1:
            return rev2019[0].Value
        return None

    def get_LastRevenue(self, obj):
        CurrentRevenue = self.context.get('CurrentRevenue')
        if not CurrentRevenue:
        # or obj.Stock_id != 3341:
            return None
        rev2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=1))
        if len(rev2018) == 1:
            return rev2018[0].Value
        return None

    def get_RevenueChange(self, obj):
        CurrentRevenue = self.context.get('CurrentRevenue')
        if not CurrentRevenue:
        # or obj.Stock_id != 3341:
            return None
        rev2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=1))
        rev2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=1))
        if len(rev2018) == 1 and len(rev2018) == 1 and rev2018[0].Value and rev2019[0].Value:
            # print(rev2018[0].Value, rev2019[0].Value, obj.Stock_id)
            return (rev2019[0].Value - rev2018[0].Value)/rev2018[0].Value
        return None

    class Meta:
        model = CompanyHistoricalQuote
        fields = '__all__'


class CompanyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTransaction
        exclude = ['Stock']


class LatestFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestFinancialInfo
        fields = '__all__'


class YearlyFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyFinancialInfo
        # exclude = ['Stock']
        fields = '__all__'


class QuarterlyFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyFinancialInfo
        # exclude = ['Stock']
        fields = '__all__'


class LastestFinancialReportsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestFinancialReportsName
        fields = '__all__'


class LastestFinancialReportsValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestFinancialReportsValue
        exclude = ['Stock']


class LastestFinancialReportsSerializer(serializers.ModelSerializer):
    Values = serializers.SerializerMethodField()

    def get_Values(self, obj):
        year = self.context.get('year')
        quarter = self.context.get('quarter')
        type = self.context.get('type')
        stock_id = self.context.get('stock_id')
        if year and quarter and type and stock_id:
            query = None
            if quarter == '0':
                # YEARLY
                YearArray = [2020, 2019, 2018, 2017, 2016, 2015, 2014]
                query = LastestFinancialReportsValue.objects.filter(
                    Q(Stock_id=stock_id)
                    & Q(Type=type)
                    & Q(ID=obj.ID) 
                    & Q(Year__in=YearArray)
                    & Q(Quarter=0)
                )
            elif quarter == '4':
                # QUARTERLY
                QuarterArray = []
                query = LastestFinancialReportsValue.objects.filter(
                    Q(Stock_id=stock_id)
                    & Q(Type=type)
                    & Q(ID=obj.ID) 
                    & (
                        (Q(Year=2020) & Q(Quarter=1))
                        | (Q(Year=2019) & Q(Quarter=4))
                        | (Q(Year=2019) & Q(Quarter=3))
                        | (Q(Year=2019) & Q(Quarter=2))
                        | (Q(Year=2019) & Q(Quarter=1))
                    )
                )
            if query:
                return LastestFinancialReportsValueSerializer(query, many=True).data
        return None

    class Meta:
        model = LastestFinancialReportsName

        fields = (
            'ID',
            'Name',
            'ParentID',
            'Expanded',
            'Level',
            'Field',
            'Values'
        )


class AnalysisSerializer(serializers.ModelSerializer):
    # StockObj = serializers.SerializerMethodField()

    # def get_StockObj(self, obj):
    #     stocks = Stock.objects.filter(id=obj.Stock_id)
    #     if stocks.count() == 1:
    #         return StockSerializer(stocks[0]).data
    #     return None

    class Meta:
        model = CompanyHistoricalQuote
        fields = '__all__'


class StockScanSerializer(serializers.ModelSerializer):
    stockId = serializers.SerializerMethodField()

    def get_stockId(self, obj):
        return obj.id

    class Meta:
        model = Stock
        fields = ['stockId']


class DecisiveIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisiveIndex
        fields = '__all__'