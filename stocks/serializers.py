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
    DecisiveIndex,
    Latest
)

from stocks.constants import IndustryTypeListStock, IndustryTypeConstant


def get_industry_type(symbol):
    if IndustryTypeListStock.TYPE_NGAN_HANG.count(symbol) > 0:
        return IndustryTypeConstant.NGAN_HANG
    elif IndustryTypeListStock.TYPE_BAO_HIEM.count(symbol) > 0:
        return IndustryTypeConstant.BAO_HIEM
    elif IndustryTypeListStock.TYPE_CHUNG_KHOAN.count(symbol) > 0:
        return IndustryTypeConstant.CHUNG_KHOAN
    elif IndustryTypeListStock.TYPE_QUY.count(symbol) > 0:
        return IndustryTypeConstant.QUY
    return IndustryTypeConstant.DEFAULT


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
                        (Q(Year=2020) & Q(Quarter=4))
                        | (Q(Year=2020) & Q(Quarter=3))
                        | (Q(Year=2020) & Q(Quarter=2))
                        | (Q(Year=2020) & Q(Quarter=1))
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


class DecisiveIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisiveIndex
        fields = '__all__'


class LatestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latest
        fields = '__all__'
