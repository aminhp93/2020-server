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
    TodayCapital = serializers.SerializerMethodField()
    PriceChange = serializers.SerializerMethodField()
    LastPrice = serializers.SerializerMethodField()
    CurrentRevenue = serializers.SerializerMethodField()
    LastRevenue = serializers.SerializerMethodField()
    RevenueChange = serializers.SerializerMethodField()
    CurrentProfit = serializers.SerializerMethodField()
    LastProfit = serializers.SerializerMethodField()
    ProfitChange = serializers.SerializerMethodField()
    PE = serializers.SerializerMethodField()
    PS = serializers.SerializerMethodField()
    PB = serializers.SerializerMethodField()
    EPS = serializers.SerializerMethodField()
    QuickRatio = serializers.SerializerMethodField()
    CurrentRatio = serializers.SerializerMethodField()
    TotalDebtOverEquity = serializers.SerializerMethodField()
    TotalDebtOverAssets = serializers.SerializerMethodField()
    TotalAssetsTurnover = serializers.SerializerMethodField()
    InventoryTurnover = serializers.SerializerMethodField()
    ReceivablesTurnover = serializers.SerializerMethodField()
    GrossMargin = serializers.SerializerMethodField()
    OperatingMargin = serializers.SerializerMethodField()
    EBITMargin = serializers.SerializerMethodField()
    NetProfitMargin = serializers.SerializerMethodField()
    ROA = serializers.SerializerMethodField()
    ROE = serializers.SerializerMethodField()
    ROIC = serializers.SerializerMethodField()


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
        Analysis = self.context.get('Analysis')
        if not Analysis:
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 1
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 112
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 1
        rev2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(rev2019) == 1:
            return rev2019[0].Value
        return None

    def get_LastRevenue(self, obj):
        Analysis = self.context.get('Analysis')
        if not Analysis:
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 1
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 112
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 1
        rev2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(rev2018) == 1:
            return rev2018[0].Value
        return None

    def get_RevenueChange(self, obj):
        Analysis = self.context.get('Analysis')
        if not Analysis:
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 1
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 112
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 1
        rev2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        rev2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(rev2018) == 1 and len(rev2018) == 1 and rev2018[0].Value and rev2019[0].Value:
            return (rev2019[0].Value - rev2018[0].Value)/rev2018[0].Value
        return None

    def get_CurrentProfit(self, obj):
        Analysis = self.context.get('Analysis')
        if not Analysis:
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 13
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 1101
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 19

        profit2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(profit2019) == 1:
            return profit2019[0].Value
        return None

    def get_LastProfit(self, obj):
        Analysis = self.context.get('Analysis')
        if not Analysis:        
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 13
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 1101
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 19

        profit2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(profit2018) == 1:
            return profit2018[0].Value
        return None

    def get_ProfitChange(self, obj):
        Analysis = self.context.get('Analysis')
        if not Analysis:
            return None
        Symbol = Stock.objects.filter(id=obj.Stock_id)[0].Symbol
        industryType = get_industry_type(Symbol)
        ID = None
        if industryType == IndustryTypeConstant.NGAN_HANG:
            ID = 13
        elif industryType == IndustryTypeConstant.BAO_HIEM:
            ID = 1
        elif industryType == IndustryTypeConstant.CHUNG_KHOAN:
            ID = 1101
        elif industryType == IndustryTypeConstant.QUY:
            ID = 1
        else:
            ID = 19
        profit2019 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2019) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        profit2018 = LastestFinancialReportsValue.objects.filter(Q(Stock_id=obj.Stock) & Q(Year=2018) & Q(Quarter=0) & Q(Type=2) & Q(ID=ID))
        if len(profit2018) == 1 and len(profit2018) == 1 and profit2018[0].Value and profit2019[0].Value:
            return (profit2019[0].Value - profit2018[0].Value)/profit2018[0].Value
        return None

    def get_PE(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].PE
        return None

    def get_PS(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].PS
        return None

    def get_PB(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].PB
        return None

    def get_EPS(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].EPS
        return None

    def get_QuickRatio(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].QuickRatio
        return None

    def get_CurrentRatio(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].CurrentRatio
        return None

    def get_TotalDebtOverEquity(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].TotalDebtOverEquity
        return None

    def get_TotalDebtOverAssets(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].TotalDebtOverAssets
        return None

    def get_TotalAssetsTurnover(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].TotalAssetsTurnover
        return None

    def get_InventoryTurnover(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].InventoryTurnover
        return None

    def get_ReceivablesTurnover(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].ReceivablesTurnover
        return None

    def get_GrossMargin(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].GrossMargin
        return None

    def get_OperatingMargin(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].OperatingMargin
        return None

    def get_EBITMargin(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].EBITMargin
        return None


    def get_NetProfitMargin(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].NetProfitMargin
        return None

    def get_ROA(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].ROA
        return None

    def get_ROE(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].ROE
        return None

    def get_ROIC(self, obj):
        xxx = LatestFinancialInfo.objects.filter(Q(Stock_id=obj.Stock))
        if len(xxx) == 1:
            return xxx[0].ROIC
        return None

    class Meta:
        model = CompanyHistoricalQuote
        fields = [
            'Stock',
            'TodayCapital',
            'PriceChange',
            'LastPrice',
            'CurrentRevenue',
            'LastRevenue',
            'RevenueChange',
            'CurrentProfit',
            'LastProfit',
            'ProfitChange',
            'DealVolume',
            'PriceClose',
            'PE',
            'PS',
            'PB',
            'EPS',
            'QuickRatio',
            'CurrentRatio',
            'TotalDebtOverEquity',
            'TotalDebtOverAssets',
            'TotalAssetsTurnover',
            'InventoryTurnover',
            'ReceivablesTurnover',
            'GrossMargin',
            'OperatingMargin',
            'EBITMargin',
            'NetProfitMargin',
            'ROA',
            'ROE',
            'ROIC'
        ]


class DecisiveIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisiveIndex
        fields = '__all__'