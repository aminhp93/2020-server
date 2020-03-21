from rest_framework import serializers

from stocks.models import (
    Stock,
    Company,
    SubCompany,
    LatestFinancialInfo,
    CompanyOfficer,
    CompanyTransaction,
    YearlyFinancialInfo,
    QuarterlyFinancialInfo
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
        # fields = '__all__'
        exclude = ['Stock']


class CompanyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOfficer
        # fields = '__all__'
        exclude = ['Stock']


class CompanyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTransaction
        # fields = '__all__'
        exclude = ['Stock']


class LatestFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestFinancialInfo
        fields = '__all__'


class YearlyFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyFinancialInfo
        # fields = '__all__'
        exclude = ['Stock']


class QuarterlyFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyFinancialInfo
        # fields = '__all__'
        exclude = ['Stock']
