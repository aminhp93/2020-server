from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel

from .constants import LastestFinancialReports


class Stock(TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, unique=True, null=False)
    Exchange = models.CharField(_('Exchange'), max_length=255, blank=True, null=False)


class Company(TimeStampedModel):
    Symbol = models.CharField(_('ICBCode'), max_length=255, blank=True, unique=True, null=False) # "FPT"
    ICBCode = models.CharField(_('ICBCode'), max_length=255, blank=True, null=True) # "9537"
    CompanyName = models.CharField(_('CompanyName'), max_length=255, blank=True, null=True) # "CTCP FPT"
    ShortName = models.CharField(_('ShortName'), max_length=255, blank=True, null=True) # "FPT Corp"
    InternationalName = models.CharField(_('InternationalName'), max_length=255, blank=True, null=True) # "FPT Corporation"
    HeadQuarters = models.CharField(_('HeadQuarters'), max_length=255, blank=True, null=True) # "Số 17, Phố Duy Tân, Phường Dịch vọng Hậu, Quận C..."
    Phone = models.CharField(_('Phone'), max_length=255, blank=True, null=True) # "+84 (24) 730-07300"
    Fax = models.CharField(_('Fax'), max_length=255, blank=True, null=True) # "+84 (24) 376-87410"
    Email = models.CharField(_('Email'), max_length=255, blank=True, null=True) # null
    WebAddress = models.CharField(_('WebAddress'), max_length=255, blank=True, null=True) # "www.fpt.com.vn"
    Overview = models.TextField(_('Overview'), blank=True, null=True) # "Nhiều năm gần đây, Công ty FPT được bình chọn là Công ty tin họ"
    History = models.TextField(_('History'), blank=True, null=True) # "<div>↵<ul>↵	<li>Ngày 13/9/1988, thành lập Công"
    BusinessAreas = models.TextField(_('BusinessAreas'), blank=True, null=True) # ""<ul>↵	<li style="text-align:justify"><span style="font-size:12px">Xây "
    Employees = models.CharField(_('Employees'), max_length=255, blank=True, null=True) # 11556
    Branches = models.CharField(_('Branches'), max_length=255, blank=True, null=True) # 17
    EstablishmentDate = models.CharField(_('EstablishmentDate'), max_length=255, blank=True, null=True) # "1988-09-13T00:00:00"
    BusinessLicenseNumber = models.CharField(_('BusinessLicenseNumber'), max_length=255, blank=True, null=True) # "0101248141 "
    DateOfIssue = models.CharField(_('DateOfIssue'), max_length=255, blank=True, null=True) # "2019-06-11T00:00:00"
    TaxIDNumber = models.CharField(_('TaxIDNumber'), max_length=255, blank=True, null=True) # "0101248141"
    CharterCapital = models.CharField(_('CharterCapital'), max_length=255, blank=True, null=True) # 6783586880000
    DateOfListing = models.CharField(_('DateOfListing'), max_length=255, blank=True, null=True) # "2006-11-21T00:00:00"
    Exchange = models.CharField(_('Exchange'), max_length=255, blank=True, null=True) # "HSX"
    InitialListingPrice = models.CharField(_('InitialListingPrice'), max_length=255, blank=True, null=True) # 400000
    ListingVolume = models.CharField(_('ListingVolume'), max_length=255, blank=True, null=True) # 678358688
    StateOwnership = models.CharField(_('StateOwnership'), max_length=255, blank=True, null=True) # 0.0596
    ForeignOwnership = models.CharField(_('ForeignOwnership'), max_length=255, blank=True, null=True) # 0.489999988206829
    OtherOwnership = models.CharField(_('OtherOwnership'), max_length=255, blank=True, null=True) # 0.450400011793171
    IsListed = models.BooleanField(_('IsListed'), default=False) # true

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.get_InternationalName

    @property
    def get_InternationalName(self):
        return self.InternationalName


class SubCompany(TimeStampedModel):
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='stock_subcompany')
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, null=True)
    InstitutionID = models.CharField(_('InstitutionID'), max_length=255, blank=True, null=True)
    Exchange = models.CharField(_('Exchange'), max_length=255, blank=True, null=True)
    CompanyName = models.CharField(_('CompanyName'), max_length=255, blank=True, null=True)
    ShortName = models.CharField(_('ShortName'), max_length=255, blank=True, null=True)
    InternationalName = models.CharField(_('InternationalName'), max_length=255, blank=True, null=True)
    CompanyProfile = models.TextField(_('CompanyProfile'), blank=True, null=True)
    Type = models.CharField(_('Type'), max_length=255, blank=True, null=True)
    Ownership = models.CharField(_('Ownership'), max_length=255, blank=True, null=True)
    Shares = models.CharField(_('Shares'), max_length=255, blank=True, null=True)
    IsListed = models.BooleanField(_('IsListed'), default=False) # true
    CharterCapital = models.CharField(_('CharterCapital'), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('SubCompany')
        verbose_name_plural = _('SubCompanies')

    def __str__(self):
        return 'SubCompany-{}-{}'.format(self.Stock_id, self.Date)


class LatestFinancialInfo(TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, unique=True, null=False) # "AAV"
    LFY = models.CharField(_('LFY'), max_length=255, blank=True, null=True) # 2019
    Year = models.CharField(_('Year'), max_length=255, blank=True, null=True) # 2019
    Quarter = models.CharField(_('Quarter'), max_length=255, blank=True, null=True) # 4
    Date = models.CharField(_('Date'), max_length=255, blank=True, null=True) # "2020-02-28T00:00:00"
    BookValuePerShare = models.CharField(_('BookValuePerShare'), max_length=255, blank=True, null=True) # 11702.509126369772
    SalesPerShare = models.CharField(_('SalesPerShare'), max_length=255, blank=True, null=True) # 20154.73321956038
    SharesOutstanding = models.CharField(_('SharesOutstanding'), max_length=255, blank=True, null=True) # 31874996
    MarketCapitalization = models.CharField(_('MarketCapitalization'), max_length=255, blank=True, null=True) # 216749972800
    PE = models.CharField(_('PE'), max_length=255, blank=True, null=True) # 7.418466458401749
    BasicPE = models.CharField(_('BasicPE'), max_length=255, blank=True, null=True) # 6.321920625456336
    DilutedPE = models.CharField(_('DilutedPE'), max_length=255, blank=True, null=True) # 7.418466458401749
    PB = models.CharField(_('PB'), max_length=255, blank=True, null=True) # 0.6448342217424873
    PS = models.CharField(_('PS'), max_length=255, blank=True, null=True) # 0.3373897300412058
    EPS = models.CharField(_('EPS'), max_length=255, blank=True, null=True) # 916.6314949498346
    BasicEPS = models.CharField(_('BasicEPS'), max_length=255, blank=True, null=True) # 1075.6224892509078
    DilutedEPS = models.CharField(_('DilutedEPS'), max_length=255, blank=True, null=True) # 916.6314949498346
    GrossMargin = models.CharField(_('GrossMargin'), max_length=255, blank=True, null=True) # 0.10473504596460788
    EBITMargin = models.CharField(_('EBITMargin'), max_length=255, blank=True, null=True) # 0.07239285911743792
    OperatingMargin = models.CharField(_('OperatingMargin'), max_length=255, blank=True, null=True) # 0.07361468044530914
    QuickRatio = models.CharField(_('QuickRatio'), max_length=255, blank=True, null=True) # 1.8344993380381511
    CurrentRatio = models.CharField(_('CurrentRatio'), max_length=255, blank=True, null=True) # 1.9848232493235696
    InterestCoverageRatio = models.CharField(_('InterestCoverageRatio'), max_length=255, blank=True, null=True) # null
    LongtermDebtOverEquity = models.CharField(_('LongtermDebtOverEquity'), max_length=255, blank=True, null=True) # null
    TotalDebtOverEquity = models.CharField(_('TotalDebtOverEquity'), max_length=255, blank=True, null=True) # 0.5779800665865592
    TotalDebtOverAssets = models.CharField(_('TotalDebtOverAssets'), max_length=255, blank=True, null=True) # 0.36627843331179016
    PreTaxMargin = models.CharField(_('PreTaxMargin'), max_length=255, blank=True, null=True) # 0.2611064692935692
    NetProfitMargin = models.CharField(_('NetProfitMargin'), max_length=255, blank=True, null=True) # 0.05626635339383114
    ROE = models.CharField(_('ROE'), max_length=255, blank=True, null=True) # 0.1077439470770574
    ROA = models.CharField(_('ROA'), max_length=255, blank=True, null=True) # 0.06293726505582908
    ROIC = models.CharField(_('ROIC'), max_length=255, blank=True, null=True) # 0.09799300843651451
    EBIT = models.CharField(_('EBIT'), max_length=255, blank=True, null=True) # 39764033130
    EBITDA = models.CharField(_('EBITDA'), max_length=255, blank=True, null=True) # 39764033130
    ROCE = models.CharField(_('ROCE'), max_length=255, blank=True, null=True) # 0.11821293393856784
    CurrentAssetsTurnover = models.CharField(_('CurrentAssetsTurnover'), max_length=255, blank=True, null=True) # 2.178631302206994
    InventoryTurnover = models.CharField(_('InventoryTurnover'), max_length=255, blank=True, null=True) # 18.54768501993482
    ReceivablesTurnover = models.CharField(_('ReceivablesTurnover'), max_length=255, blank=True, null=True) # 2.322149398043216
    TotalAssetsTurnover = models.CharField(_('TotalAssetsTurnover'), max_length=255, blank=True, null=True) # 1.1185595166494178
    ProfitFromFinancialActivitiesOverProfitBeforeTax = models.CharField(_('ProfitFromFinancialActivitiesOverProfitBeforeTax'), max_length=255, blank=True, null=True) # -0.05315645312801538
    SalesGrowth_MRQ = models.CharField(_('SalesGrowth_MRQ'), max_length=255, blank=True, null=True) # -0.3322128877152136
    SalesGrowth_MRQ2 = models.CharField(_('SalesGrowth_MRQ2'), max_length=255, blank=True, null=True) # 0.1401761823532466
    SalesGrowth_TTM = models.CharField(_('SalesGrowth_TTM'), max_length=255, blank=True, null=True) # 0.1652608873382776
    SalesGrowth_LFY = models.CharField(_('SalesGrowth_LFY'), max_length=255, blank=True, null=True) # 0.16630920913815728
    SalesGrowth_03Yr = models.CharField(_('SalesGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.5263809737779408
    ProfitGrowth_MRQ = models.CharField(_('ProfitGrowth_MRQ'), max_length=255, blank=True, null=True) # -0.7128508219041308
    ProfitGrowth_MRQ2 = models.CharField(_('ProfitGrowth_MRQ2'), max_length=255, blank=True, null=True) # 0.21047857181609667
    ProfitGrowth_TTM = models.CharField(_('ProfitGrowth_TTM'), max_length=255, blank=True, null=True) # -0.15660380305905258
    ProfitGrowth_LFY = models.CharField(_('ProfitGrowth_LFY'), max_length=255, blank=True, null=True) # -0.16215072736067948
    ProfitGrowth_03Yr = models.CharField(_('ProfitGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.3131617805798068
    BasicEPSGrowth_MRQ = models.CharField(_('BasicEPSGrowth_MRQ'), max_length=255, blank=True, null=True) # -0.8696098354945888
    BasicEPSGrowth_MRQ2 = models.CharField(_('BasicEPSGrowth_MRQ2'), max_length=255, blank=True, null=True) # -0.5475397600446555
    BasicEPSGrowth_TTM = models.CharField(_('BasicEPSGrowth_TTM'), max_length=255, blank=True, null=True) # -0.5962029916533123
    BasicEPSGrowth_LFY = models.CharField(_('BasicEPSGrowth_LFY'), max_length=255, blank=True, null=True) # -0.5472232456159267
    BasicEPSGrowth_03Yr = models.CharField(_('BasicEPSGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.09232815585403054
    DilutedEPSGrowth_MRQ = models.CharField(_('DilutedEPSGrowth_MRQ'), max_length=255, blank=True, null=True) # -0.8696098354945888
    DilutedEPSGrowth_MRQ2 = models.CharField(_('DilutedEPSGrowth_MRQ2'), max_length=255, blank=True, null=True) # -0.5475397600446555
    DilutedEPSGrowth_TTM = models.CharField(_('DilutedEPSGrowth_TTM'), max_length=255, blank=True, null=True) # -0.6181212656133894
    DilutedEPSGrowth_LFY = models.CharField(_('DilutedEPSGrowth_LFY'), max_length=255, blank=True, null=True) # -0.6141495390835081
    DilutedEPSGrowth_03Yr = models.CharField(_('DilutedEPSGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.09232815585403054
    EquityGrowth_MRQ = models.CharField(_('EquityGrowth_MRQ'), max_length=255, blank=True, null=True) # 0.8773983295411654
    EquityGrowth_TTM = models.CharField(_('EquityGrowth_TTM'), max_length=255, blank=True, null=True) # 0.8637933359907832
    EquityGrowth_03Yr = models.CharField(_('EquityGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.37658549681212716
    TotalAssetsGrowth_MRQ = models.CharField(_('TotalAssetsGrowth_MRQ'), max_length=255, blank=True, null=True) # 0.504352510286165
    TotalAssetsGrowth_MRQ2 = models.CharField(_('TotalAssetsGrowth_MRQ2'), max_length=255, blank=True, null=True) # 0.39212717609795034
    TotalAssetsGrowth_TTM = models.CharField(_('TotalAssetsGrowth_TTM'), max_length=255, blank=True, null=True) # 0.38906418351619093
    TotalAssetsGrowth_LFY = models.CharField(_('TotalAssetsGrowth_LFY'), max_length=255, blank=True, null=True) # 0.5089871244021729
    TotalAssetsGrowth_03Yr = models.CharField(_('TotalAssetsGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.19993339712796754
    CharterCapitalGrowth_MRQ = models.CharField(_('CharterCapitalGrowth_MRQ'), max_length=255, blank=True, null=True) # 1.2173916431002834
    CharterCapitalGrowth_TTM = models.CharField(_('CharterCapitalGrowth_TTM'), max_length=255, blank=True, null=True) # 1.1204817827841376
    CharterCapitalGrowth_03Yr = models.CharField(_('CharterCapitalGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.45579710770009463
    StockHolderEquityGrowth_MRQ = models.CharField(_('StockHolderEquityGrowth_MRQ'), max_length=255, blank=True, null=True) # 0.8773983295411654
    StockHolderEquityGrowth_TTM = models.CharField(_('StockHolderEquityGrowth_TTM'), max_length=255, blank=True, null=True) # 0.8637933359907832
    StockHolderEquityGrowth_03Yr = models.CharField(_('StockHolderEquityGrowth_03Yr'), max_length=255, blank=True, null=True) # 0.37658549681212716
    EBITMargin_03YrAvg = models.CharField(_('EBITMargin_03YrAvg'), max_length=255, blank=True, null=True) # 0.09112913639116545
    GrossMargin_03YrAvg = models.CharField(_('GrossMargin_03YrAvg'), max_length=255, blank=True, null=True) # 0.1279655776586451
    NetProfitMargin_03YrAvg = models.CharField(_('NetProfitMargin_03YrAvg'), max_length=255, blank=True, null=True) # 0.07119774000102208
    OperatingMargin_03YrAvg = models.CharField(_('OperatingMargin_03YrAvg'), max_length=255, blank=True, null=True) # 0.08937224762117163
    PreTaxMargin_03YrAvg = models.CharField(_('PreTaxMargin_03YrAvg'), max_length=255, blank=True, null=True) # 0.09112913639116545
    ROA_03YrAvg = models.CharField(_('ROA_03YrAvg'), max_length=255, blank=True, null=True) # 0.06891823717388257
    ROE_03YrAvg = models.CharField(_('ROE_03YrAvg'), max_length=255, blank=True, null=True) # 0.13385212567118523
    ROIC_03YrAvg = models.CharField(_('ROIC_03YrAvg'), max_length=255, blank=True, null=True) # 0.11497170668741018
    DividendInCash_03YrAvg = models.CharField(_('DividendInCash_03YrAvg'), max_length=255, blank=True, null=True) # 333.3333333333333
    DividendInShares_03YrAvg = models.CharField(_('DividendInShares_03YrAvg'), max_length=255, blank=True, null=True) # 0.049999999999999996
    FreeShares = models.CharField(_('FreeShares'), max_length=255, blank=True, null=True) # 17776246
    LastDividendInCash = models.CharField(_('LastDividendInCash'), max_length=255, blank=True, null=True) # 1000
    LastDividendInCashRecordDate = models.CharField(_('LastDividendInCashRecordDate'), max_length=255, blank=True, null=True) # "2019-06-28T00:00:00"
    NextDividendInCash = models.CharField(_('NextDividendInCash'), max_length=255, blank=True, null=True) # null
    NextDividendInCashRecordDate = models.CharField(_('NextDividendInCashRecordDate'), max_length=255, blank=True, null=True) # null
    LastDividendInShares = models.CharField(_('LastDividendInShares'), max_length=255, blank=True, null=True) # 0.15
    LastDividendInSharesRecordDate = models.CharField(_('LastDividendInSharesRecordDate'), max_length=255, blank=True, null=True) # "2018-10-04T00:00:00"
    NextDividendInShares = models.CharField(_('NextDividendInShares'), max_length=255, blank=True, null=True) # null
    NextDividendInSharesRecordDate = models.CharField(_('NextDividendInSharesRecordDate'), max_length=255, blank=True, null=True) # null
    CashDividend = models.CharField(_('CashDividend'), max_length=255, blank=True, null=True) # null
    StockDividend = models.CharField(_('StockDividend'), max_length=255, blank=True, null=True) # null
    RetentionRatio = models.CharField(_('RetentionRatio'), max_length=255, blank=True, null=True) # null
    DividendYield = models.CharField(_('DividendYield'), max_length=255, blank=True, null=True) # null
    TotalStockReturn = models.CharField(_('TotalStockReturn'), max_length=255, blank=True, null=True) # null
    CapitalGainsYield = models.CharField(_('CapitalGainsYield'), max_length=255, blank=True, null=True) # null
    PayoutRatio = models.CharField(_('PayoutRatio'), max_length=255, blank=True, null=True) # null
    LastCashDividendYear = models.CharField(_('LastCashDividendYear'), max_length=255, blank=True, null=True) # null
    LastStockDividendYear = models.CharField(_('LastStockDividendYear'), max_length=255, blank=True, null=True) # null
    COF = models.CharField(_('COF'), max_length=255, blank=True, null=True) # null
    CostToAssets = models.CharField(_('CostToAssets'), max_length=255, blank=True, null=True) # null
    CostToIncome = models.CharField(_('CostToIncome'), max_length=255, blank=True, null=True) # null
    CostToLoans = models.CharField(_('CostToLoans'), max_length=255, blank=True, null=True) # null
    EquityToLoans = models.CharField(_('EquityToLoans'), max_length=255, blank=True, null=True) # null
    LAR = models.CharField(_('LAR'), max_length=255, blank=True, null=True) # null
    LDR = models.CharField(_('LDR'), max_length=255, blank=True, null=True) # null
    LoanlossReservesToLoans = models.CharField(_('LoanlossReservesToLoans'), max_length=255, blank=True, null=True) # null
    LoanlossReservesToNPLs = models.CharField(_('LoanlossReservesToNPLs'), max_length=255, blank=True, null=True) # null
    LoansToDeposit = models.CharField(_('LoansToDeposit'), max_length=255, blank=True, null=True) # null
    NIM = models.CharField(_('NIM'), max_length=255, blank=True, null=True) # null
    NonInterestIncomeToNetInterestIncome = models.CharField(_('NonInterestIncomeToNetInterestIncome'), max_length=255, blank=True, null=True) # null
    NPLs = models.CharField(_('NPLs'), max_length=255, blank=True, null=True) # null
    NPLsToLoans = models.CharField(_('NPLsToLoans'), max_length=255, blank=True, null=True) # null
    PreprovisionROA = models.CharField(_('PreprovisionROA'), max_length=255, blank=True, null=True) # null
    ProvisionChargesToLoans = models.CharField(_('ProvisionChargesToLoans'), max_length=255, blank=True, null=True) # null
    YOEA = models.CharField(_('YOEA'), max_length=255, blank=True, null=True) # null
    PC = models.CharField(_('PC'), max_length=255, blank=True, null=True) # null
    PT = models.CharField(_('PT'), max_length=255, blank=True, null=True) # null
    Cash = models.CharField(_('Cash'), max_length=255, blank=True, null=True) # 19757069423
    TotalCurrentAssets = models.CharField(_('TotalCurrentAssets'), max_length=255, blank=True, null=True) # 320125945424
    FixedAssets = models.CharField(_('FixedAssets'), max_length=255, blank=True, null=True) # 40632023898
    TotalAssets = models.CharField(_('TotalAssets'), max_length=255, blank=True, null=True) # 588735324161
    TotalShortTermLiabilities = models.CharField(_('TotalShortTermLiabilities'), max_length=255, blank=True, null=True) # 161286878080
    TotalLiabilities = models.CharField(_('TotalLiabilities'), max_length=255, blank=True, null=True) # 215641052169
    TotalLongTermLiabilities = models.CharField(_('TotalLongTermLiabilities'), max_length=255, blank=True, null=True) # 54354174089
    TotalInventories = models.CharField(_('TotalInventories'), max_length=255, blank=True, null=True) # 24245274352
    StockHolderEquity = models.CharField(_('StockHolderEquity'), max_length=255, blank=True, null=True) # 373094271992
    GrossProfit = models.CharField(_('GrossProfit'), max_length=255, blank=True, null=True) # 13435712711
    ProfitFromFinancialActivities = models.CharField(_('ProfitFromFinancialActivities'), max_length=255, blank=True, null=True) # -2106753957
    OtherProfit = models.CharField(_('OtherProfit'), max_length=255, blank=True, null=True) # -407831462
    NetSales = models.CharField(_('NetSales'), max_length=255, blank=True, null=True) # 547472229156
    ProfitAfterIncomeTaxes = models.CharField(_('ProfitAfterIncomeTaxes'), max_length=255, blank=True, null=True) # 30804265919
    ProfitBeforeIncomeTaxes = models.CharField(_('ProfitBeforeIncomeTaxes'), max_length=255, blank=True, null=True) # 39633079956

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('LatestFinancialInfo')
        verbose_name_plural = _('LatestFinancialInfo')

    def __str__(self):
        return 'LatestFinancialInfo-{}-{}'.format(self.Symbol, self.Date)


class IntradayQuote(TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, unique=True, null=False) # "AAV"
    Date = models.CharField(_('Date'), max_length=255, blank=True) # "2020-03-02T02:06:28.88Z"
    Price = models.CharField(_('Price'), max_length=255, blank=True) # 6700
    Volume = models.CharField(_('Volume'), max_length=255, blank=True) # 3400
    TotalVolume = models.CharField(_('TotalVolume'), max_length=255, blank=True) # 12000
    Side = models.CharField(_('Side'), max_length=255, blank=True) # "S"

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('IntradayQuote')
        verbose_name_plural = _('IntradayQuotes')

    def __str__(self):
        return 'IntradayQuote-{}-{}'.format(self.Symbol, self.Date)


class HistoricalQuote(TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, unique=True, null=False) # "AAV"
    Close = models.CharField(_('Close'), max_length=255, blank=True) # 8600
    Open = models.CharField(_('Open'), max_length=255, blank=True) # 8300
    High = models.CharField(_('High'), max_length=255, blank=True) # 8600
    Low = models.CharField(_('Low'), max_length=255, blank=True) # 8300
    Volume = models.CharField(_('Volume'), max_length=255, blank=True) # 55100
    Value = models.CharField(_('Value'), max_length=255, blank=True) # 0
    Date = models.CharField(_('Date'), max_length=255, blank=True) # "2019-12-03T00:00:00Z"
    OpenInt = models.CharField(_('OpenInt'), max_length=255, blank=True) # 0

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('HistoricalQuote')
        verbose_name_plural = _('HistoricalQuotes')

    def __str__(self):
        return 'HistoricalQuote-{}-{}'.format(self.Symbol, self.Date)


class CompanyOfficer(TimeStampedModel):
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='stock_companyofficer')
    OfficerID = models.CharField(_('OfficerID'), max_length=255, blank=True)
    IndividualID = models.CharField(_('IndividualID'), max_length=255, blank=True)
    Name = models.CharField(_('Name'), max_length=255, blank=True)
    PositionID = models.CharField(_('PositionID'), max_length=255, blank=True)
    Position = models.CharField(_('Position'), max_length=255, blank=True)
    IsForeigner = models.BooleanField(_('IsForeigner'), default=False) # true

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('CompanyOfficer')
        verbose_name_plural = _('CompanyOfficers')

    def __str__(self):
        return 'CompanyOfficer-{}-{}'.format(self.Stock_id, self.Date)


class CompanyTransaction(TimeStampedModel):
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='stock_companytransaction')
    TransactionID = models.CharField(_('TransactionID'), max_length=255, blank=True, null=True)
    MajorHolderID = models.CharField(_('MajorHolderID'), max_length=255, blank=True, null=True)
    IndividualHolderID = models.CharField(_('IndividualHolderID'), max_length=255, blank=True, null=True)
    InstitutionHolderID = models.CharField(_('InstitutionHolderID'), max_length=255, blank=True, null=True)
    InstitutionHolderSymbol = models.CharField(_('InstitutionHolderSymbol'), max_length=255, blank=True, null=True)
    InstitutionHolderExchange = models.CharField(_('InstitutionHolderExchange'), max_length=255, blank=True, null=True)
    Name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
    Position = models.CharField(_('Position'), max_length=255, blank=True, null=True)
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True, null=True)
    Type = models.CharField(_('Type'), max_length=255, blank=True, null=True)
    ExecutionVolume = models.CharField(_('ExecutionVolume'), max_length=255, blank=True, null=True)
    ExecutionDate = models.CharField(_('ExecutionDate'), max_length=255, blank=True, null=True)
    StartDate = models.CharField(_('StartDate'), max_length=255, blank=True, null=True)
    EndDate = models.CharField(_('EndDate'), max_length=255, blank=True, null=True)
    RegisteredVolume = models.CharField(_('RegisteredVolume'), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('CompanyTransaction')
        verbose_name_plural = _('CompanyTransactions')

    def __str__(self):
        return 'CompanyTransaction-{}-{}'.format(self.Stock_id, self.Date)


class YearlyFinancialInfo(TimeStampedModel):
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='stock_YearlyFinancialInfo')
    Year = models.CharField(_('Year'), max_length=255, blank=True, null=True)
    DilutedEPS = models.FloatField(_('DilutedEPS'), blank=True, null=True)
    BasicEPS = models.FloatField(_('BasicEPS'), blank=True, null=True)
    DilutedEPSGrowth = models.FloatField(_('DilutedEPSGrowth'), blank=True, null=True)
    BasicEPSGrowth = models.FloatField(_('BasicEPSGrowth'), blank=True, null=True)
    DilutedEPSGrowth_03Yr = models.FloatField(_('DilutedEPSGrowth_03Yr'), blank=True, null=True)
    BasicEPSGrowth_03Yr = models.FloatField(_('BasicEPSGrowth_03Yr'), blank=True, null=True)
    GrossMargin = models.FloatField(_('GrossMargin'), blank=True, null=True)
    EBITMargin = models.FloatField(_('EBITMargin'), blank=True, null=True)
    OperatingMargin = models.FloatField(_('OperatingMargin'), blank=True, null=True)
    ProfitMargin = models.FloatField(_('ProfitMargin'), blank=True, null=True)
    QuickRatio = models.FloatField(_('QuickRatio'), blank=True, null=True)
    CurrentRatio = models.FloatField(_('CurrentRatio'), blank=True, null=True)
    ROE = models.FloatField(_('ROE'), blank=True, null=True)
    ROA = models.FloatField(_('ROA'), blank=True, null=True)
    ROIC = models.FloatField(_('ROIC'), blank=True, null=True)
    CurrentAssetsTurnover = models.FloatField(_('CurrentAssetsTurnover'), blank=True, null=True)
    InventoryTurnover = models.FloatField(_('InventoryTurnover'), blank=True, null=True)
    ReceivablesTurnover = models.FloatField(_('ReceivablesTurnover'), blank=True, null=True)
    AssetsTurnover = models.FloatField(_('AssetsTurnover'), blank=True, null=True)
    SalesGrowth = models.FloatField(_('SalesGrowth'), blank=True, null=True)
    ProfitGrowth = models.FloatField(_('ProfitGrowth'), blank=True, null=True)
    Sales = models.FloatField(_('Sales'), blank=True, null=True)
    ProfitFromOperatingActivities = models.FloatField(_('ProfitFromOperatingActivities'), blank=True, null=True)
    ProfitFromFinancialActivities = models.FloatField(_('ProfitFromFinancialActivities'), blank=True, null=True)
    ProfitBeforeTax = models.FloatField(_('ProfitBeforeTax'), blank=True, null=True)
    ProfitAfterTax = models.FloatField(_('ProfitAfterTax'), blank=True, null=True)
    Cash = models.FloatField(_('Cash'), blank=True, null=True)
    LiquidAssets = models.FloatField(_('LiquidAssets'), blank=True, null=True)
    NetLiquidAssets = models.FloatField(_('NetLiquidAssets'), blank=True, null=True)
    TotalAssets = models.FloatField(_('TotalAssets'), blank=True, null=True)
    Equity = models.FloatField(_('Equity'), blank=True, null=True)
    TotalAssetsGrowth = models.FloatField(_('TotalAssetsGrowth'), blank=True, null=True)
    EBITMargin_03YrAvg = models.FloatField(_('EBITMargin_03YrAvg'), blank=True, null=True)
    GrossMargin_03YrAvg = models.FloatField(_('GrossMargin_03YrAvg'), blank=True, null=True)
    NetProfitMargin_03YrAvg = models.FloatField(_('NetProfitMargin_03YrAvg'), blank=True, null=True)
    SalesGrowth_03Yr = models.FloatField(_('SalesGrowth_03Yr'), blank=True, null=True)
    OperatingMargin_03YrAvg = models.FloatField(_('OperatingMargin_03YrAvg'), blank=True, null=True)
    PreTaxMargin_03YrAvg = models.FloatField(_('PreTaxMargin_03YrAvg'), blank=True, null=True)
    ProfitGrowth_03Yr = models.FloatField(_('ProfitGrowth_03Yr'), blank=True, null=True)
    ROA_03YrAvg = models.FloatField(_('ROA_03YrAvg'), blank=True, null=True)
    ROE_03YrAvg = models.FloatField(_('ROE_03YrAvg'), blank=True, null=True)
    ROIC_03YrAvg = models.FloatField(_('ROIC_03YrAvg'), blank=True, null=True)
    EquityGrowth_03Yr = models.FloatField(_('EquityGrowth_03Yr'), blank=True, null=True)
    TotalAssetsGrowth_03Yr = models.FloatField(_('TotalAssetsGrowth_03Yr'), blank=True, null=True)
    LTDebtToEquity = models.FloatField(_('LTDebtToEquity'), blank=True, null=True)
    TotalDebtToEquity = models.FloatField(_('TotalDebtToEquity'), blank=True, null=True)
    BookValuePerShare = models.FloatField(_('BookValuePerShare'), blank=True, null=True)
    SalesPerShare = models.FloatField(_('SalesPerShare'), blank=True, null=True)
    TotalDebtToTotalAssets = models.FloatField(_('TotalDebtToTotalAssets'), blank=True, null=True)
    Liabilities = models.FloatField(_('Liabilities'), blank=True, null=True)
    CurrentLiabilities = models.FloatField(_('CurrentLiabilities'), blank=True, null=True)
    LongTermLiabilities = models.FloatField(_('LongTermLiabilities'), blank=True, null=True)

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('YearlyFinancialInfo')
        verbose_name_plural = _('YearlyFinancialInfo')

    def __str__(self):
        return 'YearlyFinancialInfo-{}-{}'.format(self.Stock_id, self.Date)


class QuarterlyFinancialInfo(TimeStampedModel):
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='stock_QuarterlyFinancialInfo')
    Year = models.FloatField(_('Year'), blank=True, null=True)
    Quarter = models.FloatField(_('Quarter'), blank=True, null=True)
    BasicEPS_TTM = models.FloatField(_('BasicEPS_TTM'), blank=True, null=True)
    DilutedEPS_TTM = models.FloatField(_('DilutedEPS_TTM'), blank=True, null=True)
    SalesGrowth_MRQ = models.FloatField(_('SalesGrowth_MRQ'), blank=True, null=True)
    SalesGrowth_TTM = models.FloatField(_('SalesGrowth_TTM'), blank=True, null=True)
    ProfitGrowth_MRQ = models.FloatField(_('ProfitGrowth_MRQ'), blank=True, null=True)
    ProfitGrowth_TTM = models.FloatField(_('ProfitGrowth_TTM'), blank=True, null=True)
    BasicEPSGrowth_MRQ = models.FloatField(_('BasicEPSGrowth_MRQ'), blank=True, null=True)
    BasicEPSGrowth_TTM = models.FloatField(_('BasicEPSGrowth_TTM'), blank=True, null=True)
    DilutedEPSGrowth_MRQ = models.FloatField(_('DilutedEPSGrowth_MRQ'), blank=True, null=True)
    DilutedEPSGrowth_TTM = models.FloatField(_('DilutedEPSGrowth_TTM'), blank=True, null=True)
    QuickRatio_MRQ = models.FloatField(_('QuickRatio_MRQ'), blank=True, null=True)
    CurrentRatio_MRQ = models.FloatField(_('CurrentRatio_MRQ'), blank=True, null=True)
    LTDebtToEquity_MRQ = models.FloatField(_('LTDebtToEquity_MRQ'), blank=True, null=True)
    TotalDebtToEquity_MRQ = models.FloatField(_('TotalDebtToEquity_MRQ'), blank=True, null=True)
    TotalDebtToTotalAssets_MRQ = models.FloatField(_('TotalDebtToTotalAssets_MRQ'), blank=True, null=True)
    GrossMargin_TTM = models.FloatField(_('GrossMargin_TTM'), blank=True, null=True)
    EBITMargin_TTM = models.FloatField(_('EBITMargin_TTM'), blank=True, null=True)
    OperatingMargin_TTM = models.FloatField(_('OperatingMargin_TTM'), blank=True, null=True)
    PreTaxMargin_TTM = models.FloatField(_('PreTaxMargin_TTM'), blank=True, null=True)
    NetProfitMargin_TTM = models.FloatField(_('NetProfitMargin_TTM'), blank=True, null=True)
    ROA_TTM = models.FloatField(_('ROA_TTM'), blank=True, null=True)
    ROE_TTM = models.FloatField(_('ROE_TTM'), blank=True, null=True)
    ROIC_TTM = models.FloatField(_('ROIC_TTM'), blank=True, null=True)
    InventoryTurnover_TTM = models.FloatField(_('InventoryTurnover_TTM'), blank=True, null=True)
    ReceivablesTurnover_TTM = models.FloatField(_('ReceivablesTurnover_TTM'), blank=True, null=True)
    CurrentAssetsTurnover_TTM = models.FloatField(_('CurrentAssetsTurnover_TTM'), blank=True, null=True)
    AssetsTurnover_TTM = models.FloatField(_('AssetsTurnover_TTM'), blank=True, null=True)
    DividendGrowth_MRQ = models.FloatField(_('DividendGrowth_MRQ'), blank=True, null=True)
    DividendGrowth_TTM = models.FloatField(_('DividendGrowth_TTM'), blank=True, null=True)
    TotalAssetsGrowth_MRQ = models.FloatField(_('TotalAssetsGrowth_MRQ'), blank=True, null=True)
    TotalAssetsGrowth_TTM = models.FloatField(_('TotalAssetsGrowth_TTM'), blank=True, null=True)
    BookValuePerShare_MRQ = models.FloatField(_('BookValuePerShare_MRQ'), blank=True, null=True)
    SalesPerShare_TTM = models.FloatField(_('SalesPerShare_TTM'), blank=True, null=True)
    BasicEPS_MRQ = models.FloatField(_('BasicEPS_MRQ'), blank=True, null=True)
    DilutedEPS_MRQ = models.FloatField(_('DilutedEPS_MRQ'), blank=True, null=True)
    NetSales_MRQ = models.FloatField(_('NetSales_MRQ'), blank=True, null=True)
    Dividend_MRQ = models.FloatField(_('Dividend_MRQ'), blank=True, null=True)
    TotalAssets_MRQ = models.FloatField(_('TotalAssets_MRQ'), blank=True, null=True)
    CurrentAssets_MRQ = models.FloatField(_('CurrentAssets_MRQ'), blank=True, null=True)
    Inventories_MRQ = models.FloatField(_('Inventories_MRQ'), blank=True, null=True)
    ProfitAfterTax_MRQ = models.FloatField(_('ProfitAfterTax_MRQ'), blank=True, null=True)
    SharesOutstanding_MRQ = models.FloatField(_('SharesOutstanding_MRQ'), blank=True, null=True)
    Cash_MRQ = models.FloatField(_('Cash_MRQ'), blank=True, null=True)
    NetLiquidAssets_MRQ = models.FloatField(_('NetLiquidAssets_MRQ'), blank=True, null=True)
    CurrentLiabilities_MRQ = models.FloatField(_('CurrentLiabilities_MRQ'), blank=True, null=True)
    LongTermLiabilities_MRQ = models.FloatField(_('LongTermLiabilities_MRQ'), blank=True, null=True)
    Liabilities_MRQ = models.FloatField(_('Liabilities_MRQ'), blank=True, null=True)
    Equity_MRQ = models.FloatField(_('Equity_MRQ'), blank=True, null=True)
    ProfitBeforeTax_MRQ = models.FloatField(_('ProfitBeforeTax_MRQ'), blank=True, null=True)
    FixedAssets_MRQ = models.FloatField(_('FixedAssets_MRQ'), blank=True, null=True)
    LiquidAssets_MRQ = models.FloatField(_('LiquidAssets_MRQ'), blank=True, null=True)
    IntangibleAssets_MRQ = models.FloatField(_('IntangibleAssets_MRQ'), blank=True, null=True)

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('QuarterlyFinancialInfo')
        verbose_name_plural = _('QuarterlyFinancialInfo')

    def __str__(self):
        return 'QuarterlyFinancialInfo-{}-{}'.format(self.Stock_id, self.Date)


class LastestFinancialReportsName(TimeStampedModel):
    TYPE_CHOICES = [
        (LastestFinancialReports.KQKD, '2'),
        (LastestFinancialReports.CDKT, '1'),
        (LastestFinancialReports.LCTT_TT, '3'),
        (LastestFinancialReports.LCTT_GT, '4'),
    ]

    Type = models.CharField(_('Type'), max_length=1, blank=False, null=False,
                            choices=TYPE_CHOICES, default=LastestFinancialReports.KQKD)
    ID = models.FloatField(_('ID'), blank=True, null=True)
    Name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
    ParentID = models.FloatField(_('ParentID'), blank=True, null=True)
    Expanded = models.BooleanField(_('Expanded'), default=False) # true
    Level = models.FloatField(_('Level'), blank=True, null=True)
    Field = models.CharField(_('Field'), max_length=255, blank=True, null=True)


class LastestFinancialReportsValue(TimeStampedModel):
    TYPE_CHOICES = [
        (LastestFinancialReports.KQKD, '2'),
        (LastestFinancialReports.CDKT, '1'),
        (LastestFinancialReports.LCTT_TT, '3'),
        (LastestFinancialReports.LCTT_GT, '4'),
    ]

    Type = models.CharField(_('Type'), max_length=1, blank=False, null=False,
                            choices=TYPE_CHOICES, default=LastestFinancialReports.KQKD)
    Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name='LastestFinancialReportsValue_Stock')
    ID = models.FloatField(_('ID'), blank=True, null=True)
    Period = models.CharField(_('Period'), max_length=255, blank=True, null=True)
    Year = models.FloatField(_('Year'), blank=True, null=True)
    Quarter = models.FloatField(_('Quarter'), blank=True, null=True)
    Value = models.FloatField(_('Value'), blank=True, null=True)
