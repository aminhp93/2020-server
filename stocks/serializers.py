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
    LastestFinancialReportsValue
)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SubCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCompany
        exclude = ['Stock']


class CompanyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOfficer
        exclude = ['Stock']


class CompanyHistoricalQuoteSerializer(serializers.ModelSerializer):
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
        exclude = ['Stock']


class QuarterlyFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyFinancialInfo
        exclude = ['Stock']


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
            query = LastestFinancialReportsValue.objects.filter(Q(Stock_id=stock_id) & Q(Type=type) & Q(ID=obj.ID))
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