from rest_framework import serializers

from stocks.models import Stock, Company, SubCompany, LatestFinancialInfo


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


class LatestFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestFinancialInfo
        fields = '__all__'