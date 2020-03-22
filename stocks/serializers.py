from rest_framework import serializers

from stocks.models import (
    Stock,
    Company,
    SubCompany,
    LatestFinancialInfo,
    CompanyOfficer,
    CompanyTransaction,
    YearlyFinancialInfo,
    QuarterlyFinancialInfo,
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